def base_data(folderName):
    # app.py
    app_tring = """from typing import Optional

from fastapi import FastAPI
from controllers.tasks.tasks_controller import tasks

app = FastAPI()
# tasks
app.include_router(tasks)
    """
    f = open(folderName + "/app.py", "a")

    f.write(app_tring)
    f.close()

    # entities tasks tasks.entity.py
    entity_tring = """from pydantic import BaseModel

class Task(BaseModel):
    title: str
    desc: str
    """
    f = open(folderName + "/infraestructure/entities/tasks/tasks_entity.py", "a")

    f.write(entity_tring)
    f.close()

    # controllers tasks tasks.controller.py
    controller_tring = """from infraestructure.entities.tasks.tasks_entity import Task
from fastapi import APIRouter
from domain.useCase.tasks.tasks_useCase import get_tasks_usecase, post_tasks_usecase
import sys
sys.path.append('../../')


tasks = APIRouter()


@tasks.get("/tasks")
def get_tasks():
    return get_tasks_usecase()


@tasks.post("/tasks")
def post_tasks(tasks: Task):
    return post_tasks_usecase(tasks)

    """
    f = open(folderName + "/controllers/tasks/tasks_controller.py", "a")

    f.write(controller_tring)
    f.close()

    # usecase tasks tasks_useCase.py
    usecase_tring = """from infraestructure.repository.tasks.tasks_repository import get_tasks_repository, post_tasks_repository
import sys
sys.path.append('../../../')


def get_tasks_usecase():
    return get_tasks_repository()


def post_tasks_usecase(tasks):
    return post_tasks_repository(tasks)
    """
    f = open(folderName + "/domain/useCase/tasks/tasks_useCase.py", "a")

    f.write(usecase_tring)
    f.close()

    # repository tasks tasks_repository.py
    repository_tring = """tasks_array = []

def get_tasks_repository():
    return tasks_array


def post_tasks_repository(tasks):
    tasks_array.append(tasks)
    return {"message": "Task Saved"}
    """
    f = open(folderName + "/infraestructure/repository/tasks/tasks_repository.py", "a")

    f.write(repository_tring)
    f.close()


# baseModule
def base_data_module(moduleName):
    moduleNameCapitalized = moduleName.capitalize()
    # entities moduleName moduleName.entity.py
    entity_tring = f"""from pydantic import BaseModel

class {moduleNameCapitalized}(BaseModel):
    title: str
    desc: str
    """
    f = open(
        f"infraestructure/entities/{moduleName}/{moduleName}_entity.py", "a")

    f.write(entity_tring)
    f.close()

    # controllers moduleName moduleName_controller.py
    controller_tring = f"""from infraestructure.entities.{moduleName}.{moduleName}_entity import {moduleNameCapitalized}
from fastapi import APIRouter
from domain.useCase.{moduleName}.{moduleName}_useCase import get_{moduleName}_usecase, post_{moduleName}_usecase
import sys
sys.path.append('../../')


{moduleName} = APIRouter()


@{moduleName}.get("/{moduleName}")
def get_{moduleName}():
    return get_{moduleName}_usecase()


@{moduleName}.post("/{moduleName}")
def post_{moduleName}({moduleName}: {moduleNameCapitalized}):
    return post_{moduleName}_usecase({moduleName})

    """
    f = open(f"controllers/{moduleName}/{moduleName}_controller.py", "a")

    f.write(controller_tring)
    f.close()

    # usecase moduleName moduleName_useCase.py
    usecase_tring = f"""from infraestructure.repository.{moduleName}.{moduleName}_repository import get_{moduleName}_repository, post_{moduleName}_repository
import sys
sys.path.append('../../../')


def get_{moduleName}_usecase():
    return get_{moduleName}_repository()


def post_{moduleName}_usecase({moduleName}):
    return post_{moduleName}_repository({moduleName})
    """
    f = open(f"domain/useCase/{moduleName}/{moduleName}_useCase.py", "a")

    f.write(usecase_tring)
    f.close()

    # repository moduleName moduleName_repository.py
    repository_tring = f"""{moduleName}_array = []

def get_{moduleName}_repository():
    return {moduleName}_array


def post_{moduleName}_repository({moduleName}):
    {moduleName}_array.append({moduleName})
    return "Saved"
    """
    f = open(
        f"infraestructure/repository/{moduleName}/{moduleName}_repository.py", "a")

    f.write(repository_tring)
    f.close()

# add modle to app.py


def base_data_app(moduleName):
    with open('app.py', 'r+') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            # router
            if line.startswith('app = FastAPI()'):
                lines[i] = lines[i].strip() + '\n'
                lines[i] = lines[i].strip() + f'\n# {moduleName}'
                lines[i] = lines[i].strip() + \
                    f'\napp.include_router({moduleName})'
                lines[i] = lines[i].strip() + '\n'

            # controller import
            if line.startswith('from fastapi import FastAPI'):
                lines[i] = lines[i].strip(
                ) + f'\nfrom controllers.{moduleName}.{moduleName}_controller import {moduleName}'
                lines[i] = lines[i].strip() + '\n'
        f.seek(0)
        for line in lines:
            f.write(line)
