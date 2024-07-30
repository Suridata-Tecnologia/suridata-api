from sqlalchemy import ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import mapped_column, relationship

from src.configs.database import Base


class Credential(Base):
    __tablename__ = 'credentials'

    id          = mapped_column(Integer, primary_key=True)
    company_id  = mapped_column(Integer, ForeignKey('companies.id'))
    user_id     = mapped_column(Integer, ForeignKey('users.id'))
    username    = mapped_column(String)
    password    = mapped_column(String)
    complement  = mapped_column(String)
    status      = mapped_column(Integer)
    access_type = mapped_column(String)
    operations  = mapped_column(String)
    created_at  = mapped_column(DateTime)
    updated_at  = mapped_column(DateTime)

    company = relationship('Company', back_populates='credentials')