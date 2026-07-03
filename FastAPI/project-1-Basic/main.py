from fastapi import FastAPI
import asyncio
app = FastAPI()


@app.get('/')
def home():
    return {'message': "Home page"}



@app.get('/async-await')
async def async_tutorial(): # Tells that func is asynchronus in nature -> func can be paused/resume
    db_fetch_heavy_operation = await asyncio.sleep(5) #Await - Actually pauses a function
    return db_fetch_heavy_operation
# Async - A function can be paused/resumed, so the worker can be freed for other operation in the meantime
# await - Any operation that takes time or user has to wait, only async func can contain await

'''
This is NOT Parallelism

Async Await is CONCURRENCY - worker continusously switches between tasks to check its completion, 
All handled by single worker.
In Parallelism many workers/cpu perform many tasks at the same time WITHOUT switching
'''