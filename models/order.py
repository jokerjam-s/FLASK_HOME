import datetime
from enum import Enum

from _decimal import Decimal
from pydantic import BaseModel, Field
from datetime import date
from models.user import User
from models.product import Product

from settings import settings


class StatusOrder(int, Enum):
    """Возможные статусы заказа."""

    opened = 0  # открыт
    paid = 1  # оплачен
    sent = 2  # отправлен
    returned = 3  # возврат
    canceled = 4  # отменен пользователем
    closed = 5  # завершен с ошибкой
    ok = 6  # завершен - получен


class OrderIn(BaseModel):
    """
    Заказ пользователя на товар - добавление.
    """
    users_id: int = Field(title='Код пользователя')
    products_id: int = Field(title='Код товара')
    order_date: date = Field(title="Дата")
    status: StatusOrder = Field(title="Статус", default=StatusOrder.opened.value)


class Order(OrderIn):
    """
    Заказ пользователя на товар.
    """
    id: int = Field(title="Код заказа")



