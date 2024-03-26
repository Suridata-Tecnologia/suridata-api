from pydantic import BaseModel
from datetime import date


class SinistralidadeRequest(BaseModel):
    username: str
    password: str
    start_date: date
    end_date: date


class SinistralidadeResponse(BaseModel):
    columns: list
    data: list

