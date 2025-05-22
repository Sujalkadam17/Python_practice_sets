 #installing virtual environment on PC
 pip install virtualenv
 
 python -m virtualenv env1 #creratng a virtual environment
 python -m virtualenv env2 #creratng 2nd virtual environment

.\env1\Scripts\Activate.ps1 #activating the virtual environment

#installing required dependencies for the project
 pip install pyjokes 
 pip install pyttsx
 pip freeze > requirements.txt

#deactivating the virtual environment
deactivate

#activating the 2nd virtual environment
.\env2\Scripts\Activate.ps1
#installing the dependencies from the requirements.txt file
 pip install -r requirements.txt
#deactivating the virtual environment
deactivate

#removing the virtual environments in command prompt
rmdir /s /q env1 env2