:: configure virtualenv for the project
pip install virtualenv
python -m venv .\env
cmd /k ".\env\Scripts\activate.bat & pip install -r requirements.txt"
pause
