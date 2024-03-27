from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column

from src.configs.database import Base


class Company(Base):
    __tablename__ = "companies"

    id                                = mapped_column(Integer, primary_key=True)
    status                            = mapped_column(Integer)
    pretty_name                       = mapped_column(String(100))
    name                              = mapped_column(String(100))
    drive_path                        = mapped_column(String(100))
    policy                            = mapped_column(String(100))
    suridata_product                  = mapped_column(String(100))
    dashboard_param                   = mapped_column(String(100))
