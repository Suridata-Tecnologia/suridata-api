from requests import Session
from bs4 import BeautifulSoup as BS
from datetime import datetime 
from urllib import parse
import re


class Sinistro:
    def __init__(self, session: Session, contract: dict, access_key: str) -> None:
        self.session: Session = session
        self.contract: dict = contract
        self.access_key: str = access_key


    @staticmethod
    def __response_hook(hook_data, **kwargs) -> None:
        if "Location" in hook_data.headers:
            hook_data.headers.pop('Location', None)


    def __get_download_url(self, filename: str) -> str:
        return f'https://topsaude.segurosunimed.com.br/cli/asp/download.asp?PT=Relat%F3rio%20de%20Utiliza%E7%E3o%20-%20Sinistralidade&sNomeArquivo=\\transf\\seguro_saude\\cadastro\\movimentacao\\{filename}'


    def create_job(self, start_date: datetime, end_date: datetime) -> str:
        url = 'https://topsaude.segurosunimed.com.br/itf/asp/itf0046b.asp?'
        payload = {
            'num_contrato': self.contract['code'],
            'nome_contrato': parse.quote_plus(self.contract['name'], encoding='latin1'),
            'cod_ts_contrato': '39951592',
            'dt_ini_periodo_util': start_date.strftime('%d/%m/%Y'),
            'dt_fim_periodo_util': end_date.strftime('%d/%m/%Y'),
            'txt_nome_arquivo': f'{int(datetime.now().timestamp())}.csv',
            'ind_tipo': 'D',
            'p_versao': 'Revision%3A+v12.1.3620',
            'cod_funcao': 'ITF17',
        }
        params = {
            'ID_JOB': '244',
            'p': '',
            'PT': 'Relatório de Utilização - Sinistralidade',
            'pm': '36',
            'pcf': 'ITF17',
            'pprf': 'ESTIPULANTE_EMPRESA',
            'PPRM': 'N,N,N,N,N,S',
            'tipoFuncao': 'X',
            'css': 'unimed.css',
            'codIdentificacaoTs': '39951592',
            'tipo_usuario': '2',
            'chaveAcesso': self.access_key,
        }
        url += parse.urlencode(params, encoding='latin1', quote_via=parse.quote, safe=',')

        self.session.post(url, data=payload, hooks={"response": self.__response_hook})

        url = 'https://topsaude.segurosunimed.com.br/gen/asp/gen0083a.asp?'
        params = {
            'PT': 'Relatório de Utilização - Sinistralidade',
            'IDJOB': '244',
            'COD_PARAMETRO': 'WEB_FILE_MC_GRAVA',
        }
        url += parse.urlencode(params, encoding='latin1', quote_via=parse.quote)
        response = self.session.get(url)

        soup = BS(response.text, 'html.parser')
        message = soup.select_one('p > font.msg').text
        job_id = re.findall(r'\[(.*)\]', message)[0]

        return job_id


    def get_job_status(self, job_id: str) -> dict:
        url = 'https://topsaude.segurosunimed.com.br/gen/asp/gen0083a.asp'
        params = {
            'PT': 'Relat%F3rio%20de%20Utiliza%E7%E3o%20-%20Sinistralidade',
            'cod_parametro': 'WEB_FILE_MC_GRAVA',
            'ind_popup': '',
        }
        today = datetime.today().strftime('%d/%m/%Y')
        payload = {
            'cod_usuario': 'E59943115',
            'sNomeJob': 'Relat%F3rios+de+utiliza%E7%E3o+Geral+Sinistralidade',
            'dt_ini_periodo': today,
            'dt_fim_periodo': today,
            'IdJOB': '244',
            'p_versao': 'Revision%3A+v12.1.3726',
        }
        response = self.session.post(url, params=params, data=payload)

        soup = BS(response.text, 'html.parser')

        jobs_table = soup.select('#tbl_inc_abre_table table')[-1]
        job_rows = jobs_table.select('tr')[1:]

        selected_row = None
        for row in job_rows:
            row_job_id = row.select('td')[-2].select_one('a')['href']
            row_job_id = re.findall(r"\(\'(.*)\'\)", row_job_id)[0]

            if job_id in row_job_id:
                selected_row = row
                break
        
        job_status = selected_row.select('td')[5].get_text(strip=True)
        job_filename = selected_row.select('td')[-1].get_text(strip=True)

        job = {}
        if job_status == '':
            job['status'] = 'processing'
        elif job_status == 'OK':
            job['status'] = 'done'
            job['download_url'] = self.__get_download_url(job_filename)
        else:
            job['status'] = 'error'

        return job


    def download_file(self, download_url: str) -> str:
        response = self.session.get(download_url)

        return response.content