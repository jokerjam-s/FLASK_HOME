from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from user import User
import uvicorn

app = FastAPI()

users: list[User] = []


@app.get("/", response_class=HTMLResponse)
@app.get("/index/")
async def index():
    """Отображение списка пользователей"""
    return {"index": "Start page"}


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
