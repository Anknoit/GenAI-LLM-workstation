1. Schema (Pydantic) - User Data validation before hitting API
2. Models (SQLAlchemy) - Tables for data storage after schema validation
3. Flow
4. Python Types | Type annotations
- Importatn for autocompletion help for given parameters
- Helps in Error handling for respective types (str, int, list, tuple, set)
- IDEs shows error in advance before running the endpoint if mismatch in type and input given for the parameter

```python
def add(fname: str, lname:str=None)
def bucket(fruits: list[str, str, str, int], instruction: str|bool)
    - bucket will strictly have 3 fruits and one integer 
    - instruction can either be a str or a boolean
```
5. Monolitihic Fuck - App made completely ina  framework, no interaction to third party, everything comprises inside an application as a whole from Frontend, Backend, DB etc... all in one - ex. Django application - Bank applications, security reasons

6. About FastAPI 
- Starlette - manages api request and response
- Pydantic - Data validation 
- SGI - Server Gateway interface - Protocol that converts HTTP requests for BAckend code to understand it
- Why Fast?
    - due to asynchronus nature

7. Questions
- What is oydantic models? is it the url paramaeters? where do we put it??? in app.get() or def function following it?