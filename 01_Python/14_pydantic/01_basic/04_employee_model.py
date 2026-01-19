from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=4,
        max_length=40,
        description="Employee Full Name",
        examples=["Jane Smith"],
    )

    department: Optional[str] = "Labour"
    salary: float = Field(
        ...,
        ge=100000,
        le=500000,
        description="Employee Salary",
        examples=[250000],
    )


class User(BaseModel):
    email: str = Field(
        ...,
        pattern=r"^[\w\.-]+@[\w\.-]+\.\w{2,4}$",
        description="User Email Address",
        examples=["user@example.com"],
    )

    phone: str = Field(
        ...,
        pattern=r"^\+?[1-9]\d{1,14}$",
        description="User Phone Number",
        examples=["+1234567890"],
    )
    age: int = Field(..., ge=18, le=65, description="Age in years", examples=[30])

    discount: float = Field(
        ...,
        ge=0,
        le=100,
        description="Discount Percentage",
        examples=[15.5],
    )


employee_data = {
    "id": 1,
    "name": "John Doe",
    "department": "Engineering",
    "salary": 150000,
}

user_data = {
    "email": "WaqarUlHassan@gmail.com",
    "phone": "+923249847459",
    "age": 25,
    "discount": 25.5,
}

employee = Employee(**employee_data)
print(employee)

user = User(**user_data)
print(user)
