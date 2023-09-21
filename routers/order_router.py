"""
Управление заказами пользователей.
"""
from fastapi import APIRouter
from models.order import Order, OrderIn
from models.user import User
from models.product import Product
from data.database import database, orders, users, products
from sqlalchemy import select

order_router = APIRouter()


@order_router.get('/orders')
async def get_orders():
    """
    Выбрать все заказы пользователей.

    :return:
    """
    query = (select(orders.c.id, orders.c.order_date, orders.c.status,
                    orders.c.product_id, products.c.product_name, products.c.product_descript, products.c.product_price,
                    users.c.user_family, users.c.user_name)
             .join(products).join(users))

    return await database.fetch_all(query)


@order_router.get('/orders/{order_id}')
async def get_order(order_id: int):
    """
    Выбрать заказ по номеру заказа.

    :param order_id:
    :return:
    """
    query = (select(orders.c.id, orders.c.order_date, orders.c.status,
                    orders.c.product_id, products.c.product_name, products.c.product_descript, products.c.product_price,
                    users.c.user_family, users.c.user_name)
             .join(products).join(users).where(orders.c.id == order_id))
    return await database.fetch_one(query)


@order_router.put('/orders/{order_id}', response_model=Order)
async def update_order(order_id: int, order: OrderIn):
    """
    Обновление заказа.

    :param order_id: Номер заказа.
    :param order: Изменения в заказе
    :return:
    """
    query = orders.update().where(orders.c.id == order_id).values(**order.dict())
    await database.execute(query)
    return {**order.dict(), "id": order_id}


@order_router.post('/orders', response_model=Order)
async def insert_product(new_order: OrderIn):
    """
    Добавление нового заказа.

    :param new_order: Информация о новом заказе.
    :return:
    """
    query = orders.insert().values(
        users_id = new_order.users_id,
        products_id = new_order.products_id,
        order_date = new_order.order_date,
        status = new_order.status
    )
    last_order_id = await database.execute(query)
    return {**new_order.dict(), "id": last_order_id}


@order_router.delete('/orders/{order_id}')
async def delete_product(order_id: int):
    """
    Удаление заказа.

    :param order_id: Номер удаляемого заказа.
    :return:
    """
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return {'message': 'Product deleted'}