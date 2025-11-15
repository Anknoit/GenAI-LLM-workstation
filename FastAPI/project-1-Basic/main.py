from fastapi import FastAPI

from typing import Union

app = FastAPI()

@app.get("/")
def homepage():
    return {"Welcome to Homepage"}
k
@app.get()
def 
