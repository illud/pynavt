from setuptools import setup, find_packages

setup(
    name='pynavt',
    version='1.0.0',
    author='Alejandro Castillo Valdes',
    author_email='saturnavt@gmail.com',
    description='pynavt is a tool to create a clean architecture project and auto generating modules',
    license='MIT',
    url='https://github.com/saturnavt/pynavt',
    packages=find_packages(),
    py_modules=['pynavt', 'base'],
    install_requires=[
        'click',
        'fastapi',
        'uvicorn',
        'pydantic'
    ],
    entry_points='''
        [console_scripts]
        pynavt=pynavt.__init__:main
    ''',
)
