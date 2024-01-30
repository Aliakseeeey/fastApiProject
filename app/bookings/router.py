from fastapi import APIRouter, Depends
from app.bookings.dao import BookingDAO
from app.users.dependencies import get_current_user
from app.users.models import User
from app.bookings.schemas import SBooking

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"]
)


@router.get("")
async def get_booking(user: User = Depends(get_current_user)): # -> list[SBooking]:
    return await BookingDAO.find_all(use_id=user.id)
