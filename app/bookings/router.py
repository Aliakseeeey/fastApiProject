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
async def get_booking(user: User = Depends(get_current_user)) -> list[SBooking]:
    return await BookingDAO.find_all(user_id=user.id)


@router.post("")
async def add_booking(
        room_id: int, date_from: int,
        user: User = Depends(get_current_user),
):
    await BookingDAO.add(user.id, room_id, date_from)