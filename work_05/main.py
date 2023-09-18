import os.path
from enum import Enum

from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from work_05.Model.user import User
import uvicorn

base_dir = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(base_dir, 'templates')
static_dir = os.path.join(base_dir, 'static')

app = FastAPI()
# https://qna.habr.com/q/1219276
# https://metanit.com/python/fastapi/1.9.php
app.mount('/static', StaticFiles(directory=static_dir), name="static")
templates = Jinja2Templates(directory=templates_dir)

users: list[User] = []


@app.get("/", response_class=HTMLResponse)
@app.get("/index/", response_class=HTMLResponse)
async def index(request: Request):
    """Отображение списка пользователей"""
    context = {"request": request, "users": users}
    return templates.TemplateResponse("main.html", context=context)


@app.delete('/user/{id}')
async def delete_user(id: int):
    """
    Удаление пользователя.

    :param id: идентификатор удаляемого пользователя
    :return:
    """
    user = [u for u in users if u.id == id]
    if len(user) > 0:
        users.remove(user[0])
        return {'message': 'User deleted'}
    return {'message': 'User not found'}


@app.put('/user/{id}')
async def update_user(id: int, user_info: User):
    """
    Обновление информации о пользователе.

    :param id: идентификатор пользователя для обновления
    :param user: новая информация о пользователе
    :return:
    """
    user = [u for u in users if u.id == id]
    user_info.id = id
    if len(user) > 0:
        users[users.index(user[0])] = user_info
        return {'message': 'User updated'}
    return user_info

def get_next_id(users: list[User]) -> int:
    """
    Поиск максимального идентификатора в списке пользователей.

    :param users: cписок пользователей
    :return: значение для нового id
    """
    next_id = 0
    if len(users) > 0:
        next_id = users[-1].id
    return next_id + 1



@app.post('/user/add/')
async def insert_user(user: User):
    user.id = get_next_id(users)
    users.append(user)
    return user


if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8200, reload=True)
