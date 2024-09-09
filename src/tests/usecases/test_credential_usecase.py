from unittest.mock import MagicMock, Mock
from sqlalchemy.orm import Session

from src.schemas.credential import Credential
from src.schemas.company import Company
from src.repositories.credential import CredentialRepository
from src.usecases.credential import CredentialUseCase
from src.repositories.company import CompanyRepository


def test_list_all():
    mock_db = MagicMock(spec=Session)
    mock_credential_1 = {
        'id': 1,
        'username': 'test_username',
        'password': 'test_password',
        'complement': 'test_complement',
        'status': 1,
        'operations': 'premio,sinistralidade',
        'company': {
            'id': 1,
            'name': 'test_company',
            'policy': 'test_policy',
            'status': 0,
            'drive_path': 'test_drive_path',
            'dashboard_param': 'test_dashboard_param',
            'suridata_product': 'test_suridata_product'
        }
    }
    mock_credential_2 = {
        'id': 2,
        'username': 'test_username',
        'password': 'test_password',
        'complement': 'test_complement',
        'status': 2,
        'operations': 'senhas,sinistro',
        'company': {
            'id': 2,
            'name': 'test_company',
            'policy': 'test_policy',
            'status': 1,
            'drive_path': 'test_drive_path',
            'dashboard_param': 'test_dashboard_param',
            'suridata_product': 'test_suridata_product'
        }
    }

    mock_credential_1 = Credential(**mock_credential_1)
    mock_credential_2 = Credential(**mock_credential_2)
    mock_credentials = [mock_credential_1, mock_credential_2]

    CredentialRepository.find_all = Mock(return_value=mock_credentials)

    result = CredentialUseCase.list_all(mock_db)

    assert result == mock_credentials


def should_raise_error_on_company_not_found():
    mock_db = MagicMock(spec=Session)

    mock_company = {
        'id': 1,
        'status': 1,
        'pretty_name': 'Empresateste',
        'name': 'Teste',
        'drive_path': 'TESTE_AMIL',
        'policy': '12345',
        'suridata_product': 'Controle',
        'dashboard_param': 'Teste Amil'
    }
    
    mock_company = Company(**mock_company)

    CompanyRepository.find_by_id = Mock(return_value=mock_company)
    

    result = CredentialUseCase.list_all(mock_db)

    assert result == mock_credentials