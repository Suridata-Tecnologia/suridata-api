from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from typing import List, Union

from ..configs.database import get_db
from ..usecases.credential import CredentialUseCase
from ..schemas.credential import CredentialOut, CredentialIn 


router = APIRouter(prefix='/credentials')

@router.get('/', response_model=List[CredentialOut])
async def list(
    db: Session = Depends(get_db),
    
) -> List[CredentialOut]:
    return CredentialUseCase.list_all(db)


@router.get('/items')
async def read_item(q: Union[str, None] = None):
    return {'q': q}


@router.post('/')
async def create_credential(credential: CredentialIn, db: Session = Depends(get_db)):
    return CredentialUseCase.create_credential(db, credential)
    
    