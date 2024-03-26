from sqlalchemy import Integer, String, Column
from src.configs.database import Base


class Company(Base):
    __tablename__ = "companies"

    id                                = Column(Integer, primary_key=True)
    status                            = Column(Integer)
    pretty_name                       = Column(String(100))
    name                              = Column(String(100))
    drive_path                        = Column(String(100))
    policy                            = Column(String(100))
    multiple_policies                 = Column(String(100))
    suridata_product                  = Column(String(100))
    name_contact_in_health_brokerage  = Column(String(100))
    email_contact_in_health_brokerage = Column(String(200))
    dashboard_param                   = Column(String(100))
