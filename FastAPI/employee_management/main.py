from fastapi import FastAPI
import json
app = FastAPI()

# Helpler Funtion

def load_file():
    with open('employee.json', 'r') as f:
        data = json.load(f)
    return data


@app.get('/')
def home():
    return {'message': 'Home Page'}


@app.get('/view')
def view():
    data = load_file()
    return data