from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column

from src.configs.database import Base


class Operator(Base):
    __tablename__ = "operators"

    id   = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(100))
