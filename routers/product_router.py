"""
Работа с информацией о продуктах в магазине.
"""
from fastapi import APIRouter
from data.database import database, products
from models.product import Product, ProductIn

product_router = APIRouter()


@product_router.get('/products', response_model=list[Product])
async def get_products():
    """
    Получение списка реализуемых продуктов.

    :return:
    """
    query = products.select()
    return await database.fetch_all(query)


@product_router.get('/products/{product_id}', response_model=Product)
async def get_product(product_id: int):
    """
    Получение продукта по идентификатору.

    :param product_id:
    :return:
    """
    query = products.select().where(products.c.id == product_id)
    return await database.fetch_one(query)


@product_router.put('/products/{product_id}', response_model=Product)
async def update_product(product_id: int, product: ProductIn):
    """
    Изменение информации о продукте.

    :param product_id: Код изменяемого продукта.
    :param product: Информация о продукте.
    :return:
    """
    query = products.update().where(products.c.id == product_id).values(**product.dict())
    await database.execute(query)
    return {**product.dict(), "id": product_id}


@product_router.post('/products', response_model=Product)
async def insert_product(new_prod: ProductIn):
    """
    Добавление нового продукта.

    :param new_prod: Информация о добавляемом продукте.
    :return:
    """
    query = products.insert().values(
        product_name=new_prod.product_name,
        product_descript=new_prod.product_descript,
        product_price=new_prod.product_price
    )
    last_prod_id = await database.execute(query)
    return {**new_prod.dict(), "id": last_prod_id}


@product_router.delete('/products/{product_id}')
async def delete_product(product_id: int):
    """
    Удаление продукта.

    :param product_id: Код удаляемого продукта.
    :return:
    """
    query = products.delete().where(products.c.id == product_id)
    await database.execute(query)
    return {'message': 'Product deleted'}
