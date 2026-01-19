from typing import List, Optional
from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class User(BaseModel):
    id: int
    name: str
    address: Address


# Creating a User instance using a dictionary for the nested Address model
print("Creating User with nested Address model : ")

address = Address(street="123 Main St", city="Capetown", postal_code="12345")
user = User(id=1, name="John Doe", address=address)
print(user)

# Creating a User instance using a dictionary for the nested Address model
print("\nCreating User from dictionary data : ")

user_data = {
    "id": 2,
    "name": "Jane Smith",
    "address": {"street": "123 Main St", "city": "Capetown", "postal_code": "12345"},
}
user2 = User(**user_data)
print(user2)