"""
Работа с пользователями системы.
"""
from fastapi import APIRouter
from models.user import UserIn, User
from data.database import users, database

user_router = APIRouter()


@user_router.get('/users', response_model=list[User])
async def get_users():
    """
    Список всех пользователей.

    :return:
    """
    query = users.select()
    return await database.fetch_all(query)


@user_router.get('/users/{user_id}', response_model=User)
async def get_user(user_id: int):
    """
    Возврат конкретного пользователя.

    :param user_id: Код искомого пользователя
    :return:
    """
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@user_router.put('/users/{user_id}', response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), "id": user_id}


@user_router.delete('/users/{user_id}')
async def delete_user(user_id: int):
    """
    Удаление пользователя.

    :param user_id: Код удаляемого пользователя
    :return:
    """
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}


@user_router.post('/users', response_model=User)
async def insert_user(new_user: UserIn):
    """
    Добавление нового пользователя.

    :param new_user: Информация о новом пользователе
    :return:
    """
    query = users.insert().values(
        user_family=new_user.user_family,
        user_name=new_user.user_name,
        user_email=new_user.user_email,
        user_password=new_user.user_password
    )
    last_user_id = await database.execute(query)
    return {**new_user.dict(), "id": last_user_id}
