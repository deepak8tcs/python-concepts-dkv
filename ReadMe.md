
#Setting up virtual env(venv for python3) for python project:

503174398@GPF1QLRZFE MINGW64 /c/GitCode/gehc-edison-ai-rawdicom-lib (master)

$ python -V   //py -V //py works in Python terminal
Python 3.7.6  

$ python -m venv env   //py -m venv env  /2nd arg is the location to create the virtual environment. 


$ source env/Scripts/activate  //bash terminal
(env)
C:\GitCode\python-concepts-dkv>.\env\Scripts\activate  //Python terminal
(env) C:\GitCode\python-concepts-dkv>


//install the python dependencies/libraries
$ pip install -r requirements.txt


//Running a python file
$ python src/client_scripts/GI_Edison_FileManager.py  //py xyz.py