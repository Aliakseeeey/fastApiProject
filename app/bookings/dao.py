from app.database import async_session_maker
from app.bookings.models import Bookings
from sqlalchemy import select, delete, insert, func, and_, or_
from app.dao.base import BaseDAO


class BookingDAO(BaseDAO):
    model = Bookings

    @classmethod
    async def add(
            cls,
            room_id: int,
            date_from: int,
    ):
        booked_rooms = select(Bookings).where(
            and_(
                Bookings.id == 1,
                or_(
                    and_(
                        Bookings.date_from >= date_from,
                        Bookings.date_from <= date_from
                    )
                )
            )
        ).cte("booked_rooms")
