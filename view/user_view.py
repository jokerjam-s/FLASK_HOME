from fastapi import APIRouter
from models.user import UserIn, User
from data.database import users, database

route = APIRouter()


@route.get('/users', response_model=list[User])
async def get_users():
    """
    Список всех пользователей.
    :return:
    """
    query = users.select()
    return await database.fetch_all(query)


@route.get('/get_user/{user_id}', response_model=User)
async def get_user(user_id: int):
    """
    Возврат конкретного пользователя.
    :param user_id: код искомого пользователя
    :return:
    """
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@route.put('/users/{user_id}', response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    database.execute(query)
    return {**new_user.dict(), "id": user_id}


@route.delete('/users/{user_id}')
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    database.execute(query)
    return {'message': 'User deleted'}