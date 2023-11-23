from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def fio():
    return{"FIO": "Cherevkov Mikhail Andreevich"}

@app.get('/users')
async def personal_info():
    return{"phone number": "+79133661385", "email" : "mikhailcherevkov@gmail.com"}

@app.get('/tools')
async def skills():
    return{"Навыки разработчика": "Змейка на Python"}
