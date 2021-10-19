
## Setting up virtual env(venv for python3) for python project:
# Checking python version installed:

py -V 
or
python -V 

At root folder of project:
python -m venv env
or
py -m venv env
# 2nd arg is the location to create the virtual environment. 

 //bash terminal
source env/Scripts/activate 
(env)
//Python terminal
C:\GitCode\python-concepts-dkv>.\env\Scripts\activate  
(env) C:\GitCode\python-concepts-dkv>


## install the python dependencies/libraries
$ pip install -r requirements.txt


## Running a python file
$ python src/client_scripts/GI_Edison_FileManager.py
or
py xyz.py

python -m venv c:\path\to\myenv   #no need of git ignore then 
=============================
## To open python console
$py
>>>print("hi")
>>>exit() #to exit python console

## pip: pip is a reference to python package manager,comes bundled with python

pip install requests                #latest version

pip install requests==2.18.4        #sepecific version

pip install requests>=2.0.0,<3.0.0  #latest 2.x release of requests:

pip install --upgrade requests      #uninstall old version and installs latest version

pip install -r requirements.txt     #we use -r flag here

## Instead of installing packages individually, pip allows you to declare all dependencies in a Requirements File.
requirements.txt
requests==2.18.4
google-auth==1.1.0

## Pip can export a list of all installed packages and their versions using the freeze command:
pip freeze

Which will output a list of package specifiers such as:

cachetools==2.0.1

certifi==2017.7.27.1

chardet==3.0.4

This is useful for creating Requirements Files that can re-create the exact versions of 
all packages installed in an environment.

## Notes:
we can use IDLE shell as well to type and run python code.
we can use either single quotes or double quotes for string.

