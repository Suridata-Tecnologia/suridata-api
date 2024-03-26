from pydantic import BaseModel
from datetime import date


class PremioRequest(BaseModel):
    username: str
    password: str
    competence: date


class PremioResponse(BaseModel):
    file_content: str