import click
import os

# base
from pynavt.base import base_data, base_data_module, base_data_app, base_db_client

print("""
      _____                         _   
     |  __ \                       | |  
     | |__) |   _ _ __   __ ___   _| |_ 
     |  ___/ | | | '_ \ / _` \ \ / / __|
     | |   | |_| | | | | (_| |\ V /| |_ 
     |_|    \__, |_| |_|\__,_| \_/  \__|
             __/ |                      
            |___/ 
       ----------------------------------
      |  pynavt --new yourProjectName    |
      |  pynavt --module yourModuleName  |
      |  pynavt --client mysql           |
       ------------=Alejandro Castillo=--                      
""")


@click.command()
@click.option("--new", help="Generates new project")
@click.option("--module", help="Generates new module")
@click.option("--client", help="Generates new database client")
def main(new, module, client):
    if new != None:
        os.makedirs(new, exist_ok=True)
        print("Project generated")
        # main.py
        open(new + '/' + 'main.py', 'w')
        print("main.py generated")

        # Controllers
        os.makedirs(new + "/controllers", exist_ok=True)
        print("Controllers folder generated")
        # controller tasks
        os.makedirs(new + "/controllers/tasks", exist_ok=True)
        print("Task folder generated")
        open(new + '/controllers/tasks/' + 'tasks_controller.py', 'w')

        # domain
        os.makedirs(new + "/domain", exist_ok=True)
        print("Domain folder generated")

        # useCase
        os.makedirs(new + "/domain/useCase", exist_ok=True)
        print("UseCase folder generated")
        # domain useCase tasks
        os.makedirs(new + "/domain/useCase/tasks", exist_ok=True)
        print("Task folder generated")
        open(new + '/domain/useCase/tasks/' + 'tasks_useCase.py', 'w')

        # infraestructure
        os.makedirs(new + "/infraestructure", exist_ok=True)
        print("Infraestructure folder generated")
        # infraestructure repository
        os.makedirs(new + "/infraestructure/repository", exist_ok=True)
        print("Infraestructure repository folder generated")
        # infraestructure repository tasks
        os.makedirs(new + "/infraestructure/repository/tasks", exist_ok=True)
        print("Infraestructure repository tasks folder generated")
        # infraestructure repository tasks tasks.repository.py
        open(new + '/infraestructure/repository/tasks/' +
             'tasks_repository.py', 'w')
        print("infraestructure repository tasks tasks_repository.py generated")

        # infraestructure databases
        os.makedirs(new + "/infraestructure/databases", exist_ok=True)
        print("Infraestructure databases folder generated")
        # infraestructure databases client.py
        open(new + '/infraestructure/databases/' + 'client.py', 'w')
        print("infraestructure databases client.go generated")

        # infraestructure entities
        os.makedirs(new + "/infraestructure/entities", exist_ok=True)
        print("Infraestructure entities folder generated")
        # infraestructure entities tasks
        os.makedirs(new + "/infraestructure/entities/tasks", exist_ok=True)
        print("Infraestructure entities tasks folder generated")
        # infraestructure entity tasks tasks.entity.py
        open(new + '/infraestructure/entities/tasks/' + 'tasks_entity.py', 'w')
        print("infraestructure entity tasks tasks_entity.py generated")

        # utils
        os.makedirs(new + "/utils", exist_ok=True)
        print("Utils folder generated")
        # utils errors
        os.makedirs(new + "/utils/errors", exist_ok=True)
        print("Utils errors folder generated")
        # utils errors errors.py
        open(new + '/utils/errors/' + 'errors.py', 'w')
        print("Utils errors  errors.py generated")

        # utils services
        os.makedirs(new + "/utils/services", exist_ok=True)
        print("Services folder generated")

        # utils services bcrypt
        os.makedirs(new + "/utils/services/bcrypt", exist_ok=True)
        print("Utils services bcrypt folder generated")
        # utils services bcrypt.py
        open(new + '/utils/services/bcrypt/' + 'bcrypt.py', 'w')
        print("Utils services bcrypt bcrypt.py generated")

        # utils services jwt
        os.makedirs(new + "/utils/services/jwt", exist_ok=True)
        print("Utils services jwt folder generated")
        # utils services jwt.py
        open(new + '/utils/services/jwt/' + 'jwt.py', 'w')
        print("Utils services jwt jwt.py generated")

        # create base data
        base_data(new)

        # get started
        print(f"""
      _____                         _   
     |  __ \                       | |  
     | |__) |   _ _ __   __ ___   _| |_ 
     |  ___/ | | | '_ \ / _` \ \ / / __|
     | |   | |_| | | | | (_| |\ V /| |_ 
     |_|    \__, |_| |_|\__,_| \_/  \__|
             __/ |                      
            |___/ 
       ----------------------------------
      |           Get started            |
      |            cd {new}              |
      |     uvicorn main:app --reload    |
       ------------=Alejandro Castillo=--
        """)

    if module != None:
        directory_path = os.getcwd()

        # entity
        os.makedirs(directory_path + "/infraestructure/entities/" +
                    module, exist_ok=True)
        print(module + " folder generated")
        open(directory_path + '/infraestructure/entities/' + module +
             '/' + module + '_entity.py', 'w')

        # controller module
        os.makedirs(directory_path + "/controllers/" + module, exist_ok=True)
        print(module + " folder generated")
        open(directory_path + '/controllers/' + module +
             '/' + module + '_controller.py', 'w')

        # usecase module
        os.makedirs(directory_path + "/domain/useCase/" +
                    module, exist_ok=True)
        open(directory_path + '/domain/useCase/' + module +
             '/' + module + '_useCase.py', 'w')

        # repository module
        os.makedirs(directory_path + "/infraestructure/repository/" +
                    module, exist_ok=True)
        open(directory_path + '/infraestructure/repository/' + module +
             '/' + module + '_repository.py', 'w')

        # adds data to module
        base_data_module(module)

        # adds to main.py
        base_data_app(module)

    if client != None:
        base_db_client(client)


if __name__ == '__main__':
    main()
