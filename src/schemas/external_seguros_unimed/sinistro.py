from pydantic import BaseModel
from datetime import date


class SinistroRequest(BaseModel):
    username: str
    password: str
    start_date: date
    end_date: date


class SinistroCreateJobResponse(BaseModel):
    job_id: int


class SinistroFetchJobResponse(BaseModel):
    status: str
    download_url: str