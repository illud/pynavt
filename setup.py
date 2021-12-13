from setuptools import setup, find_packages

# readme.me
with open("README.md", "r") as fh:
    long_description = fh.read()

# twine command
# python setup.py sdist bdist_wheel
# twine upload dist/*
setup(
    name='pynavt',
    version='1.0.8',
    author='Alejandro Castillo Valdes',
    author_email='saturnavt@gmail.com',
    description='pynavt is a tool to create a clean architecture project and auto generating modules',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url='https://github.com/saturnavt/pynavt',
    packages=find_packages(),
    py_modules=['pynavt', 'base'],
    install_requires=[
        'click',
        'fastapi',
        'uvicorn',
        'pydantic',
        'bcrypt',
        'pyjwt'
    ],
    entry_points='''
        [console_scripts]
        pynavt=pynavt.__init__:main
    ''',
)
