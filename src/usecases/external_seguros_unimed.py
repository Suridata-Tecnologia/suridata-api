from ..schemas.external_seguros_unimed.sinistro import SinistroFetchJobResponse, SinistroRequest
from ..schemas.external_seguros_unimed.sinistralidade import SinistralidadeRequest, SinistralidadeResponse
from ..schemas.external_seguros_unimed.premio import PremioRequest, PremioResponse
from ..scraping.seguros_unimed.SegurosUnimed import SegurosUnimed


class ExternalSegurosUnimedUseCase:
    @staticmethod
    def get_premio(request: PremioRequest) -> PremioResponse:
        api = SegurosUnimed(request.username, request.password)
        content = api.premio.get_premio(request.competence)

        return content


    @staticmethod
    def get_sinistralidade(request: SinistralidadeRequest) -> SinistralidadeResponse:
        api = SegurosUnimed(request.username, request.password)
        content = api.sinistralidade.get_sinistralidade(request.start_date, request.end_date)

        return content


    @staticmethod
    def create_sinistro_job(request: SinistroRequest) -> int:
        api = SegurosUnimed(request.username, request.password)
        job_id = api.sinistro.create_job(request.start_date, request.end_date)

        return job_id


    @staticmethod
    def fetch_job_status(job_id: int) -> SinistroFetchJobResponse:
        api = SegurosUnimed()
        job_id = api.sinistro.create_job(request.start_date, request.end_date)

        return job_id