import sqlalchemy
from sqlalchemy import create_engine
import databases as databases
from sqlalchemy import Table, Column, Integer, String, Numeric, Date, Text, ForeignKey

from settings import settings

DATABASE_URL = settings.DATABASE_URL
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

# Таблица пользователей, должна содержать следующие поля: id (PRIMARY KEY), имя, фамилия,
#   адрес электронной почты и пароль.
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_family", String(settings.USER_NAME_LEN), nullable=False),
    Column("user_name", String(settings.USER_NAME_LEN), nullable=False),
    Column("user_email", String(settings.EMAIL_LEN), nullable=False),
    Column("user_password", String(settings.PASSWORD_MAX_LEN), nullable=False),
)

# Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.
products = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("product_name", String(settings.PRODUCT_NAME_LEN), nullable=False),
    Column("product_descript", Text),
    Column("product_price", Numeric(10, 2), default=0),
)

# Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id пользователя (FOREIGN KEY),
#   id товара (FOREIGN KEY), дата заказа и статус заказа.
orders = Table(
    "orders",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("product_id", Integer, ForeignKey("products.id")),
    Column("order_date", Date, nullable=False),
    Column("status", Integer, default=0, nullable=False),
)

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

metadata.create_all(engine)
