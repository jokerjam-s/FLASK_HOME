import os.path
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import uvicorn
from data.database import database

# get routers
from routers import user_router, product_router, order_router

# application path settings
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")

# start application
app = FastAPI()

# mount directories & templates
# app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
# templates = Jinja2Templates(directory=TEMPLATES_DIR)

# start app
app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get('/')
async def home():
    return {'message': 'application started'}


app.include_router(user_router.user_router, tags=['users'])
app.include_router(product_router.product_router, tags=['products'])
app.include_router(order_router.order_router, tags=['orders'])

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
