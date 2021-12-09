# Pynavt

```
  _____                         _   
 |  __ \                       | |  
 | |__) |   _ _ __   __ ___   _| |_ 
 |  ___/ | | | '_ \ / _` \ \ / / __|
 | |   | |_| | | | | (_| |\ V /| |_ 
 |_|    \__, |_| |_|\__,_| \_/  \__|
         __/ |                      
        |___/                       
```
## Create project with Clean Architecture folder structure

\
Pynavt is a cli tool to create clean architecture app for you including Fastapi, bcrypt and jwt.

- Creates Clean Architecture project for you


## Features
- Clean Architecture Folder Structure (https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- Fastapi (https://fastapi.tiangolo.com/)
- Jwt (https://pyjwt.readthedocs.io/)
- Bcrypt (https://pypi.org/project/bcrypt/)
- Auto generate module
- Auto generate db service client 
  - Mysql
- Example tasks api

## Installation

Pynavt requires [Python](https://www.python.org/) 3.6 to run.

Install the dependencies.

```sh
pip install pynavt
```


## How to use

In your terminal type to see all avaible commands:

```sh
pynavt
```

To create a new Fastapi with clean architecture project(This includes a crud example with the name of Tasks):

```
pynavt --new yourProjectName
```

To create a new module with crud:

```
pynavt --module yourModuleName
```

To run the project:

```
uvicorn app:app --relaod
```

## Database service
To create a new db service client with Mysql:

Mysql - to learn more visit (https://www.w3schools.com/python/python_mysql_getstarted.asp)
```
pynavt --client mysql
```

### This will generate a database connection in infraestructure/databases/client.py
### to use import the service in your repository.




## Folder Structure:

```

|-- controller
|        |      
|        |-tasks --> This is and example folder(Create your own folder)
|            |       
|            |-tasks_controller.py --> This is and example controller file(Create your own controllers)
|            
|-- domain
|      |
|      |-useCase
|            |
|            |-tasks --> This is and example folder(Create your own folder)
|                | 
|                |-task_useCase.py --> This is and example useCase file(Create your own useCases)
|
|-- infraestructure
|           |
|           |-databases
|           |      |
|           |      |-client.py
|           |
|           |-entities
|           |      |
|           |      |-tasks --> This is and example folder(Create your own folder)
|           |          |
|           |          |-tasks_entity.py --> This is and example entity file(Create your own entity)
|           |
|           |-respository
|                  |
|                  |-tasks --> This is and example folder(Create your own folder)
|                      | 
|                      |-tasks_repository.py --> This is and example repository file(Create your own repositories)
|                       
|-- utils
        |
        |-errors
        |    |
        |    |-errros.py
        |
        |-services
                |
                |-jwt
                |   |
                |   |-jwt.py
                |
                |-bcrypt
                    |
                    |-bcrypt.py
```

## License

MIT

Pynavt is [MIT licensed](LICENSE)."# Pynavt" 
"# pynavt" 
"# pynavt" 
