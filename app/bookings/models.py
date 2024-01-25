from app.database import Base
from sqlalchemy import Column, Integer, String, JSON, ForeignKey, Date, Time


class Bookings(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)
    salon_id = Column(ForeignKey("salons.id"))
    user_id = Column(ForeignKey("user.id"))
    date_from = Column(Date, nullable=False)
    time_from = Column(Time, nullable=False)
    price = Column(Integer, nullable=False)