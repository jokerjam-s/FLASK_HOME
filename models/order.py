import datetime
from enum import Enum

from pydantic import BaseModel, Field
from datetime import date


class StatusOrder(int, Enum):
    """Возможные статусы заказа."""

    opened: 0  # открыт
    paid: 1  # оплачен
    sent: 2  # отправлен
    returned: 3  # возврат
    canceled: 4  # отменен пользователем
    closed: 5  # завершен с ошибкой
    ok: 6  # завершен - получен


class Order(BaseModel):
    """
    Заказ пользователя на товар.
    """
    id: int = Field(title="Код заказа")
    user_id: int = Field(title="Пользователь")
    product_id: int = Field(title="Продукт")
    order_date: date = Field(title="Дата")
    status: StatusOrder = Field(title="Статус", default=StatusOrder.opened)


class OrderIn(BaseModel):
    """
    Заказ пользователя на товар - добавление.
    """
    user_id: int = Field(title="Пользователь")
    product_id: int = Field(title="Продукт")
    order_date: date = Field(title="Дата")
    status: StatusOrder = Field(title="Статус", default=StatusOrder.opened)
