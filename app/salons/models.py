from app.database import Base
from sqlalchemy import Column, Integer, String, JSON


class Salons(Base):
    __tablename__ = "salons"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    services = Column(JSON)
    image_id = Column(Integer)