from pydantic import BaseModel, field_validator
from datetime import datetime


class User(BaseModel):
    first_name: str
    last_name: str

    @field_validator("first_name", "last_name")
    def name_must_be_capitalized(cls, value):
        if not value.istitle():
            raise ValueError("Name must be capitalized")
        return value


class User(BaseModel):
    email: str

    @field_validator("email")
    def normalize_email(cls, value):
        return value.lower().strip()


class Product(BaseModel):
    price: str

    @field_validator("price", mode="before")
    def validate_price(cls, value):
        if isinstance(value, str):
            return float(value.replace("$", ""))
        return value


class DateRange(BaseModel):
    start_date: datetime
    end_date: datetime

    @field_validator(mode="after")
    def check_date_order(cls, value):
        if value.start_date >= value.end_date:
            raise ValueError("start_date must be before end_date")
        return value
    
    
user = User(first_name="John", last_name="Doe")
print(user)

user_email = User(email="Example@Email.com")
print(user_email)

product = Product(price="$19.99")
print(product)

date_range = DateRange(start_date="2023-01-01", end_date="2023-12-31")
print(date_range)