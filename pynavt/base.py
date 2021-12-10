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
    id: int
    title: str
    desc: str
    """
    f = open(folderName + "/infraestructure/entities/tasks/tasks_entity.py", "a")

    f.write(entity_tring)
    f.close()

    # controllers tasks tasks.controller.py
    controller_tring = """from infraestructure.entities.tasks.tasks_entity import Task
from fastapi import APIRouter
from domain.useCase.tasks.tasks_useCase import get_tasks_usecase, post_tasks_usecase, delete_tasks_usecase, update_tasks_usecase
import sys
sys.path.append('../../')


tasks = APIRouter()


@tasks.get("/tasks")
def get_tasks():
    return get_tasks_usecase()


@tasks.post("/tasks")
def post_tasks(tasks: Task):
    return post_tasks_usecase(tasks)


@tasks.put("/tasks/{id}")
def update_tasks(tasks: Task, id):
    return update_tasks_usecase(tasks, id)


@tasks.delete("/tasks/{id}")
def delete_tasks(id):
    return delete_tasks_usecase(id)
    """
    f = open(folderName + "/controllers/tasks/tasks_controller.py", "a")

    f.write(controller_tring)
    f.close()

    # usecase tasks tasks_useCase.py
    usecase_tring = """from infraestructure.repository.tasks.tasks_repository import get_tasks_repository, post_tasks_repository, delete_tasks_repository, update_tasks_repository
import sys
sys.path.append('../../../')


def get_tasks_usecase():
    return get_tasks_repository()


def post_tasks_usecase(tasks):
    return post_tasks_repository(tasks)


def update_tasks_usecase(tasks, id):
    return update_tasks_repository(tasks, id)


def delete_tasks_usecase(id):
    return delete_tasks_repository(id)
    """
    f = open(folderName + "/domain/useCase/tasks/tasks_useCase.py", "a")

    f.write(usecase_tring)
    f.close()

    # repository tasks tasks_repository.py
    repository_tring = """tasks_array = []


def get_tasks_repository():
    return tasks_array


def post_tasks_repository(tasks):
    tasks_array.append(
        {"id": tasks.id, "title": tasks.title, "desc": tasks.desc})
    return {"message": "Task Saved"}


def update_tasks_repository(tasks, id):
    for i in range(len(tasks_array)):
        if tasks_array[i]['id'] == int(id):
            tasks_array[i]['title'] = tasks.title
            tasks_array[i]['desc'] = tasks.desc
    return {"message": "Task Updated"}


def delete_tasks_repository(id):
    for i in range(len(tasks_array)):
        if tasks_array[i]['id'] == int(id):
            del tasks_array[i]
            break
    return {"message": "Task Deleted"}
    """
    f = open(folderName + "/infraestructure/repository/tasks/tasks_repository.py", "a")

    f.write(repository_tring)
    f.close()

    # bcrypt bcrypt.py
    bcrypt_tring = """import bcrypt

#hash password
def hash(password):
	hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(10))
	return hashed


# check hashed password
def check_hash(password, hash):
	if bcrypt.checkpw(password.encode('utf-8'), hash):
		return True
	else:
		return False
            """
    f = open(folderName + "/utils/services/bcrypt/bcrypt.py", "a")
    print("Bcrypt created")
    f.write(bcrypt_tring)
    f.close()

    # jwt jwt.py
    jwt_tring = """import jwt


def generate_token(payload):
	return jwt.encode({"some": payload}, "secret", algorithm="HS256")


def validate_token(token):
	return jwt.decode(token, "secret", algorithms=["HS256"])
            """
    f = open(folderName + "/utils/services/jwt/jwt.py", "a")
    print("Jwt created")
    f.write(jwt_tring)
    f.close()

    # errors errors.py
    errors_tring = """# You can add your own errors
bad_request = {"Error": "Bad Request", "Code": 400}
forbidden = {"Error": "Forbidden", "Code": 403}
not_found = {"Error": "Not Found", "Code": 404}
unauthorized = {"Error": "Unauthorized", "Code": 401}
            """
    f = open(folderName + "/utils/errors/errors.py", "a")
    print("Errors created")
    f.write(errors_tring)
    f.close()


# baseModule
def base_data_module(moduleName):
    moduleNameCapitalized = moduleName.capitalize()
    # entities moduleName moduleName.entity.py
    entity_tring = f"""from pydantic import BaseModel

class {moduleNameCapitalized}(BaseModel):
    id: int
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
from domain.useCase.{moduleName}.{moduleName}_useCase import get_{moduleName}_usecase, post_{moduleName}_usecase, delete_{moduleName}_usecase, update_{moduleName}_usecase
import sys
sys.path.append('../../')


{moduleName} = APIRouter()


@{moduleName}.get("/{moduleName}")
def get_{moduleName}():
    return get_{moduleName}_usecase()


@{moduleName}.post("/{moduleName}")
def post_{moduleName}({moduleName}: {moduleNameCapitalized}):
    return post_{moduleName}_usecase({moduleName})

@{moduleName}.put("/{moduleName}/{"{id}"}")
def update_{moduleName}({moduleName}: {moduleNameCapitalized}, id):
    return update_{moduleName}_usecase({moduleName}, id)


@{moduleName}.delete("/{moduleName}/{"{id}"}")
def delete_{moduleName}(id):
    return delete_{moduleName}_usecase(id)
    """
    f = open(f"controllers/{moduleName}/{moduleName}_controller.py", "a")

    f.write(controller_tring)
    f.close()

    # usecase moduleName moduleName_useCase.py
    usecase_tring = f"""from infraestructure.repository.{moduleName}.{moduleName}_repository import get_{moduleName}_repository, post_{moduleName}_repository, delete_{moduleName}_repository, update_{moduleName}_repository
import sys
sys.path.append('../../../')


def get_{moduleName}_usecase():
    return get_{moduleName}_repository()


def post_{moduleName}_usecase({moduleName}):
    return post_{moduleName}_repository({moduleName})

def update_{moduleName}_usecase({moduleName}, id):
    return update_{moduleName}_repository({moduleName}, id)


def delete_{moduleName}_usecase(id):
    return delete_{moduleName}_repository(id)
    """
    f = open(f"domain/useCase/{moduleName}/{moduleName}_useCase.py", "a")

    f.write(usecase_tring)
    f.close()

    # repository moduleName moduleName_repository.py
    repository_tring = f"""{moduleName}_array = []

def get_{moduleName}_repository():
    return {moduleName}_array


def post_{moduleName}_repository({moduleName}):
    {moduleName}_array.append({"{'id': %s.id, 'title': %s.title, 'desc': %s.desc}" % (moduleName, moduleName, moduleName)})
    return {"{'message':'Saved'}"}


def update_{moduleName}_repository({moduleName}, id):
    for i in range(len({moduleName}_array)):
        if {moduleName}_array[i]['id'] == int(id):
            {moduleName}_array[i]['title'] = {moduleName}.title
            {moduleName}_array[i]['desc'] = {moduleName}.desc
    return {"{'message':'Updated'}"}


def delete_{moduleName}_repository(id):
    for i in range(len({moduleName}_array)):
        if {moduleName}_array[i]['id'] == int(id):
            del {moduleName}_array[i]
            break
    return {"{'message':'Deleted'}"}
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


# db client
def base_db_client(client):
    if client == "mysql":
        # client moduleName client.py
        db_client_tring = """import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="youruserName",
    password="yourPassword",
    database="yourDatabaseName"
)

db = mydb.cursor(dictionary=True)
            """
        f = open(
            "infraestructure/databases/client.py", "a")
        print("Mysql client created")
        f.write(db_client_tring)
        f.close()
