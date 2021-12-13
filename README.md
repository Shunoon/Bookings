# Schwack booking script
&nbsp;
##  For windows
Create new virtual environment:
```
python -m venv venv
```
To activate on CMD:
```
<path to venv>\Scripts\activate.bat
```

After that install Selenium and Webdriver:
```
pip install -r requirements.txt
```
To run the script:
```
<path to python> Book.py <name> <email> <phone> <showingnumber> <seats seperated by comma>

Example: python Book.py Jhon jhon123@gmail.com 7123456 1 C8,C9,C10
```
## For Unix
Create new virtual environment:
```
python3 -m venv venv
```
To activate on CMD:
```
source venv/bin/activate
```
After that install Selenium and Webdriver:
```
pip install -r requirements.txt
```
To run the script:
```
<path to python> Book.py <name> <email> <phone> <showingnumber> <seats seperated by comma>

Example: python Book.py Jhon jhon123@gmail.com 7123456 1 C8,C9,C10