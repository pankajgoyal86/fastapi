## To create a new environment
python -m venv .venv


## To activate
source .venv/bin/activate
## To see all packages
pip list
## To save to a file
pip freeze > requirements.txt

## to install all dependencies from file
pip install -r requirements.txt

## to install pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.pycurl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 -m pip --version
python3 -m pip install -r requirements.txt


## to run main.py
python3 -m pip install -r requirements.txt && python3 -m uvicorn main:app --reload

##to run docs
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc
