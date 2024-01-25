from pydantic import BaseModel
from datetime import date, time


class SBooking(BaseModel):
    id: int
    salon_id: int
    user_id: int
    date_from: date
    time_from: time
    price: int

    class Config:
        orm_mode = True
