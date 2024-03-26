from fastapi import APIRouter

from ..usecases.external_seguros_unimed import ExternalSegurosUnimedUseCase
from ..schemas.external_seguros_unimed.premio import PremioRequest, PremioResponse
from ..schemas.external_seguros_unimed.sinistralidade import SinistralidadeRequest, SinistralidadeResponse
from ..schemas.external_seguros_unimed.sinistro import SinistroRequest, SinistroCreateJobResponse


router = APIRouter(prefix='/external/seguros-unimed')

@router.post('/premio', response_model=PremioResponse)
def premio(request: PremioRequest) -> PremioResponse:
    content = ExternalSegurosUnimedUseCase.get_premio(request)

    return PremioResponse(content)


@router.post('/sinistralidade', response_model=SinistralidadeResponse)
def sinistralidade(request: SinistralidadeRequest) -> SinistralidadeResponse:
    content = ExternalSegurosUnimedUseCase.get_sinistralidade(request)

    return SinistralidadeResponse(**content)


@router.post('/sinistro', response_model=SinistroCreateJobResponse)
def create_job(request: SinistroRequest) -> SinistroCreateJobResponse:
    job_id = ExternalSegurosUnimedUseCase.create_sinistro_job(request)

    return SinistroCreateJobResponse(job_id=job_id)


@router.put('/sinistro/{job_id}', response_model=SinistroCreateJobResponse)
def create_job(job_id: str) -> SinistroCreateJobResponse:
    job_status = ExternalSegurosUnimedUseCase.
    return job_status

