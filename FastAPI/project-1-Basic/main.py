from fastapi import FastApi

app = FastApi()


app.get('/')
def home():
    return {'message': "Home page"}

app.get('/about')
