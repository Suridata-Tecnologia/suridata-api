from requests import Session
from bs4 import BeautifulSoup as BS
from datetime import datetime 
import pandas as pd


class Sinistralidade:
    def __init__(self, session: Session, contract: dict) -> None:
        self.session: Session = session
        self.contract: dict = contract

        self.start_date: dict = {}
        self.end_date: dict = {}


    @staticmethod
    def __extract_data_from_html(html) -> str:
        soup = BS(html, 'html.parser')
        message = soup.select_one('.msg').get_text()

        if 'processamento do tipo Competencia' in message:
            return None

        table = soup.select_one('#tbl_inc_abre_table table.sortable')
        df = pd.read_html(table.prettify())[0]

        return df.to_dict(orient="split", index=False)


    def __set_date_range(self, start_date: datetime, end_date: datetime) -> None:
        self.start_date = start_date.strftime('%m/%Y')
        self.end_date = end_date.strftime('%m/%Y')


    def __request_by_group(self) -> str:
        url = 'https://topsaude.segurosunimed.com.br/ger/asp/ger1038z.asp'
        params = {
            'pt': 'Sinistralidade por Grupo',
            'tela': 'M',
            'cod_grupo_empresa': self.contract['code'],
            'nome_grupo_empresa': self.contract['name'],
            'ind_tipo_sinistro': '1',
            'dt_ini_periodo': self.start_date,
            'dt_fim_periodo': self.end_date,
            'mes_ano_ref': '01/2024',
        }
        payload = {
            'p_versao': 'Revision: v12.1.2988',
            'p_ind_tipo_sinistro': '1',
            'cod_grupo_empresa': self.contract['code'],
            'nome_grupo_empresa': self.contract['name'],
            'mes_ano_ref': '01/2024',
            'opt_ind_tipo_sinistro': '1',
            'ind_tipo_periodo': 'D',
            'dt_ini_periodo': self.start_date,
            'dt_fim_periodo': self.end_date,
            'ind_tipo': 'P',
            'qtd_limite': '10000',
            'ind_ordenacao': 'C',
            'pgm_retorno': '/ger/asp/ger0029a.asp?pt=Sinistralidade por Grupo&ind_tipo_sinistro=',
            'OperadoraTS': '30',
        }
        response = self.session.post(url, params=params, data=payload)

        data = self.__extract_data_from_html(response.text)

        return data


    def __request_by_comp(self) -> str:
        url = 'https://topsaude.segurosunimed.com.br/ger/asp/ger0029z.asp'
        params = {
            'pt': 'Sinistralidade por Grupo',
            'tela': 'M',
            'ind_tipo_sinistro': '2',
            'dt_ini_periodo': self.start_date,
            'dt_fim_periodo': self.end_date,
            'mes_ano_ref': '10/2023',
        }
        payload = {
            'p_versao': 'Revision: v12.1.2988',
            'p_ind_tipo_sinistro': '2',
            'num_contrato': self.contract['code'],
            'nome_contrato': self.contract['name'],
            'cod_ts_contrato': '39951592',
            'mes_ano_ref': '10/2023',
            'opt_ind_tipo_sinistro': '2',
            'ind_tipo_periodo': 'D',
            'dt_ini_periodo': self.start_date,
            'dt_fim_periodo': self.end_date,
            'ind_tipo': 'P',
            'qtd_limite': '1000',
            'ind_ordenacao': 'C',
            'pgm_retorno': '/ger/asp/ger0029a.asp?pt=Sinistralidade por Grupo&ind_tipo_sinistro=',
            'OperadoraTS': '30',
        }
        response = self.session.post(url, params=params, data=payload)

        data = self.__extract_data_from_html(response.text)

        return data


    def get_sinistralidade(self, start_date: datetime, end_date: datetime) -> str:
        self.__set_date_range(start_date, end_date)

        data = self.__request_by_group()

        if not data:
            data = self.__request_by_comp()

        return data