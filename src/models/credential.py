from sqlalchemy import ForeignKey, Integer, String, DateTime, Column
from datetime import datetime, timezone

from src.configs.database import Base


class Credential(Base):
    __tablename__ = 'credentials'

    id          = Column(Integer, primary_key=True)
    company_id  = Column(Integer, ForeignKey('companies.id'), nullable=False)
    user_id     = Column(Integer, ForeignKey('users.id'), nullable=False)
    username    = Column(String, nullable=False)
    password    = Column(String, nullable=False)
    complement  = Column(String)
    status      = Column(Integer, nullable=False)
    access_type = Column(String)
    operations  = Column(String, nullable=False)
    created_at  = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at  = Column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
