from typing import Optional
from pydantic import BaseModel, Field



class Company(BaseModel):
    id: int
    name: Optional[str]
    policy: Optional[str]
    status: int
    drive_folder: Optional[str] = Field(alias='drive_path')
    corporate_name: Optional[str] = Field(alias='name')
    params: Optional[str] = Field(alias='dashboard_param')
    product: Optional[str] = Field(alias='suridata_product')

    class Config:
        from_attributes = True