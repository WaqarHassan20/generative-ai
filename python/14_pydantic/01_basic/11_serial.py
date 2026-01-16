from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import List


class Address(BaseModel):
    zip_code: str
    city: str
    street: str


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool
    createdAt: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime("%d-%m-%Y %H:%M:%S"),
        }
    )


user = User(
    id=1,
    name="John Doe",
    email="john.doe@example.com",
    is_active=True,
    createdAt=datetime(2024, 6, 1, 14, 30, 0),
    address=Address(zip_code="12345", city="New York", street="123 Main St"),
    tags=["admin", "user"],
)

python_dict = user.model_dump()

print(user.model_dump_json())

print("-"* 20)

print(python_dict)