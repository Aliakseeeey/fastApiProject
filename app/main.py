from fastapi import FastAPI, Query, Depends
from typing import Optional
from datetime import date, time
from pydantic import BaseModel

app = FastAPI()


# class SMaster(BaseModel):
#     address: str
#     name_master: str
#     stars: int
class MasterSearchArgs:
    def __init__(self,
                 name_city: str,
                 date_from: date,
                 time_from: time,
                 comment: Optional[str] = None,
                 home_visit: Optional[bool] = None,
                 stars: Optional[int] = Query(None, ge=1, le=5),
                 ):
        self.name_city = name_city
        self.date_from = date_from
        self.time_from = time_from
        self.comment = comment
        self.home_visit = home_visit
        self.stars = stars


@app.get("/city")
async def root(
        search_args: MasterSearchArgs = Depends()
):
    return search_args


class SReserved(BaseModel):
    master_id: int
    date_from: date
    time_from: time


@app.post("/reserved")
async def add_reserved(reserved: SReserved):
    pass
