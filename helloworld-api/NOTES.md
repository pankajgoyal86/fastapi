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