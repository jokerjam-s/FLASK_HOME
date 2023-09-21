from decimal import Decimal

from pydantic import BaseModel, Field
from settings import settings
from typing import Optional


class Product(BaseModel):
    """
    Реализуемые товары в магазине.
    """
    id: int = Field(title="Код продукта")
    product_name: str = Field(
        title="Наименование", max_length=settings.PRODUCT_NAME_LEN
    )
    product_descript: Optional[str] = Field(title="Описание")
    product_price: Decimal = Field(title="Цена", ge=0, default=0)


class ProductIn(BaseModel):
    """
    Реализуемые товары - модель добавления.
    """
    product_name: str = Field(
        title="Наименование", max_length=settings.PRODUCT_NAME_LEN
    )
    product_descript: Optional[str] = Field(title="Описание")
    product_price: Decimal = Field(title="Цена", ge=0, default=0)
