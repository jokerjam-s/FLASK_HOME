import os.path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from work_05.user import User
import uvicorn

base_dir = os.path.dirname(os.path.abspath(__file__))
print(base_dir)
app = FastAPI()
# https://qna.habr.com/q/1219276
app.mount(base_dir, StaticFiles(directory='static'), name="work_05")
templates = Jinja2Templates(directory='work_05/templates')

users: list[User] = []


@app.get("/", response_class=HTMLResponse)
@app.get("/index/", response_class=HTMLResponse)
async def index(request: Request):
    """Отображение списка пользователей"""
    return templates.TemplateResponse("main.html", {"request": request, "users": users})


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
    else:
        pass


@app.put('/user/{id}')
async def update_user(id: int, user_info: User):
    """
    Обновление информации о пользователе.

    :param id: идентификатор пользователя для обновления
    :param user: новая информация о пользователе
    :return:
    """
    user = [u for u in users if u.id == id]
    if len(user) > 0:
        users[users.index(user[0])] = user_info


def get_max_id(users: list[User]) -> int:
    """
    Поиск максимального идентификатора в списке пользователей.

    :param users: cписок пользователей
    :return: найденное значение, если список пуст - 0
    """
    max_id = 0
    for user in users:
        if user.id > max_id:
            max_id = user.id
    return max_id


@app.post('/user/')
async def insert_user(user: User):
    user.id = get_max_id(users) + 1
    users.append(user)


if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8200, reload=True)
