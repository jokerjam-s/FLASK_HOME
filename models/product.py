from decimal import Decimal

from pydantic import BaseModel, Field
from settings import settings
from typing import Optional

class Product(BaseModel):
    id: int = Field(title='Код продукта')
    product_name: str = Field(title='Наименование', max_length=settings.PRODUCT_NAME_LEN)
    product_descript: Optional[str] = Field(title='Описание')
    product_price: Decimal = Field(title='Цена', ge=0)
