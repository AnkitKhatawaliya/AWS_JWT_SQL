from fastapi import FastAPI
from Routers.User import router as UserRouter

app = FastAPI()

@app.get('/')
def BaseRoot():
    return {"The Backend": "Is Working"}

app.include_router(UserRouter,prefix= "",tags="User")