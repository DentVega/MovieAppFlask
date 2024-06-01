# Guia de Instalación del interprete 

### Paso: 1

Ejecuta el comando `pip3 install virtualenv`

### Paso: 2

Ejecuta el comando `python -m virtualenv venv`

### Paso: 3

#### Visual Studio code:

3.1: Instala la extension Python.

>Name: Python
>Id: ms-python.python
>Description: Python language support with extension access points for IntelliSense (Pylance), Debugging (Python Debugger), linting, formatting, refactoring, unit tests, and more.
>Version: 2024.6.0
>Publisher: Microsoft
>>VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-python.python

3.2 Presione F1 en VSCode y seleccione la opcion `Select interpreter`

![Select interpreter in VSCode](./readmeFiles/selectInterpreter.png "Command Palette")

3.3 Seleccione el archivo python en la direccion `env/bin/python`

![python in the venv folder](./readmeFiles/venvPython.png "options interpreter")