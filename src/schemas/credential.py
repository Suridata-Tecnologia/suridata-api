from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, field_validator

from ..schemas.company import Company


class OperationsEnum(str, Enum):
    premio: str         = 'premio'
    sinistro: str       = 'sinistro'
    sinistralidade: str = 'sinistralidade'
    senhas: str         = 'senhas'


class Credential(BaseModel):
    id: int
    username: str
    password: str
    complement: Optional[str]
    status: str
    operations: List[OperationsEnum]
    company: Optional[Company]

    @field_validator('status', mode='before')
    def parse_status(cls, value):
        return 'active' if value else 'inactive'

    @field_validator('operations', mode='before')
    def parse_operations(cls, value):
        return [OperationsEnum(i.lower()) for i in value.split(',')]

    class ConfigDict:
        from_attributes = True