from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, field_validator

from ..schemas.company import Company
# from ..schemas.users import Users 


class OperationsEnum(str, Enum):
    premio: str         = 'premio'
    sinistro: str       = 'sinistro'
    sinistralidade: str = 'sinistralidade'
    senhas: str         = 'senhas'


class CredentialOut(BaseModel):
    id: int
    username: str
    password: str
    complement: Optional[str]
    status: str
    operations: List[OperationsEnum]
    user_id: int

    @field_validator('status', mode='before')
    def parse_status(cls, value):
        return 'active' if value else 'inactive'

    @field_validator('operations', mode='before')
    def parse_operations(cls, value):
        return [OperationsEnum(i) for i in value.split(',')]
    
    class ConfigDict:
        from_attributes = True


class CredentialIn(BaseModel):
    username: str
    password: str
    complement: Optional[str] = None
    access_type: str = 'suridata'
    status: int
    operations: List[OperationsEnum]
    company_id: int

    @field_validator('operations', mode='after')
    def join_operations(cls, value):
        return ','.join(value)


    class ConfigDict:
        from_attributes = True 