from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def f_index():
    return{"message": "Hello!"}

@app.get('/tools')
async def f_indexT():
    return{"message": "Tools", "key" : "Привет!"}

#new