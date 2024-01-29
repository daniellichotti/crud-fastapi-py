# Linux
## creating virtual env
python3 -m venv env
## activating virtual env
source env/bin/activate

## install requirements
pip install -r requirements.txt

## run server
uvicorn main:app --reload
## run tests
python3 baterAPI.py
