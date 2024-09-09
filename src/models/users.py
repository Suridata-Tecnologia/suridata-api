from sqlalchemy import Integer, String, TIMESTAMP, DATETIME, BIGINT
from sqlalchemy.orm import mapped_column, relationship

from src.configs.database import Base

class Users(Base):
    __tablename__ = "users"

    id                      = mapped_column(BIGINT, primary_key=True)
    name                    = mapped_column(String(255))
    email                   = mapped_column(String(255))
    email_send_at           = mapped_column(DATETIME(100))
    password                = mapped_column(String(100))
    access                  = mapped_column(Integer)
    company                 = mapped_column(Integer)
    view_dash               = mapped_column(Integer)
    see_margin              = mapped_column(Integer)
    remember_token          = mapped_column(String(100))
    created_at              = mapped_column(TIMESTAMP)
    updated_at              = mapped_column(TIMESTAMP)
    inactive                = mapped_column(Integer)
    email_verified_at       = mapped_column(DATETIME)
    received_email          = mapped_column(Integer)
    is_suridata_user        = mapped_column(Integer)
    is_business_user        = mapped_column(Integer)
    language_id             = mapped_column(Integer)
    status_policy           = mapped_column(String(255))
    response_date_policy    = mapped_column(String(255))
    has_suriwallet_access   = mapped_column(String(255))
    birthday                = mapped_column(String(255))


    # credentials_users = relationship('Credential', back_populates='users')
