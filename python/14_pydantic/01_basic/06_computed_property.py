from pydantic import BaseModel, Field, computed_field


class Product(BaseModel):
    price: float
    quantity: int

    @computed_field  # it is telling pydantic that this is a computed property
    @property  # it is telling that how to access that computed property or value
    def total_cost(self) -> float:
        return self.price * self.quantity


class Booking(BaseModel):

    user_id: int
    room_id: int
    nights: int = Field(
        ...,
        ge=1,
        description="Number of nights, must be at least 1",
    )
    rate_per_night: float

    @computed_field
    @property
    def total_amount(self) -> float:
        return self.nights * self.rate_per_night
    

room_booking = Booking(
    user_id=123,
    room_id=456,
    nights=3,
    rate_per_night=150.0,
)

print("Room Booking Data:", room_booking.model_dump())
print("Room Booking Amount:", room_booking.total_amount)