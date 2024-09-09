from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime


class Users(BaseModel):
    id :int
    name :Optional[str]
    email :Optional[str]
    email_send_at: Optional[datetime]
    password : str
    access : int
    company : int
    view_dash : Optional[int]
    see_margin : Optional[int]
    remember_token : Optional[str]
    created_at : Optional[datetime]
    updated_at : Optional[datetime]
    inactive : Optional[int]
    email_verified_at : Optional[datetime]
    received_email : Optional[int]
    is_suridata_user : Optional[int]
    is_business_user : Optional[int]
    language_id : Optional[int]
    status_policy : Optional[str]
    response_date_policy : Optional[str]
    has_suriwallet_access : Optional[str]
    birthday : Optional[str]

    class ConfigDict:
        from_attribute: True


class UserBase(BaseModel):
    username: str
    password: str
    email: str