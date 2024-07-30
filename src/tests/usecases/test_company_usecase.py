from unittest.mock import MagicMock, Mock
from sqlalchemy.orm import Session

from src.schemas.company import Company
from src.repositories.company import CompanyRepository
from src.usecases.company import CompanyUseCase


def test_find_all():
    mock_db = MagicMock(spec=Session)
    mock_company_1 = Company(
        id=1,
        status=1,
        pretty_name="Company 1",
        name="Company1",
        drive_path="DRIVE_TESTE",
        policy="1234s",
        suridata_product='Test Product',
        dashboard_param='1234asdc'
    )
    mock_company_2 = Company(
        id=2,
        status=1,
        pretty_name="Company 1",
        name="Company1",
        drive_path="DRIVE_TESTE",
        policy="1234s",
        suridata_product='Test Product',
        dashboard_param='1234asdc'
    )
    mock_companies = [mock_company_1, mock_company_2]

    CompanyRepository.find_all = Mock(return_value=mock_companies)

    result = CompanyUseCase.list_all(mock_db)

    assert result == mock_companies