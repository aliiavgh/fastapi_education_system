from fastapi import FastAPI

app = FastAPI(title='Udemy clone')

@app.get('/')
def hello(): 
    return 'Hello World'