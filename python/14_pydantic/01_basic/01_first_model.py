from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    is_active: bool


# Creating an instance of the User model
user = User(id=1, name="Paul", is_active=True)
print(user)

# Creating an instance from a dictionary
input_data = {"id": 2, "name": "Tom", "is_active": False}
user = User(**input_data)
print(user)

# Creating an instance with wrong data types (will raise a validation error)
# user = User(id=1, name="Paul", is_active=25)
# print(user)