from datetime import datetime
from bs4 import BeautifulSoup as BS
from urllib import parse
from requests import Session
import re


class Premio:
    def __init__(self, session: Session) -> None:
        self.session: Session = session
        self.available_competences: list = self.__set_available_competences()


    def __set_available_competences(self) -> list:
        url = 'https://topsaude.segurosunimed.com.br/fat/asp/fat0000b.asp?cpaint_function=CarregaComboMesAno&cpaint_argument[]=1&cpaint_argument[]=&cpaint_response_type=TEXT'

        response = self.session.get(url)

        decoded_html = bytes(response.text, 'utf-8').decode('unicode_escape')
        soup = BS(decoded_html, 'html.parser')
        options = soup.select('option')[1:]

        return [option.get_text(strip=True) for option in options]


    def __request_file(self, competence: datetime) -> str:
        payload = {
            'ind_tipo_pessoa': 'J',
            'cod_operadora': '1',
            'hidden_vld_cod_operadora': 'S',
            'hidden_cod_operadora_msg': 'Operadora+n%E3o+informada.',
            'cod_sucursal': '1',
            'hidden_vld_cod_sucursal': 'S',
            'hidden_cod_sucursal_msg': 'Filial+n%E3o+informada.',
            'cod_inspetoria_ts': '1',
            'hidden_vld_cod_inspetoria_ts': 'S',
            'hidden_cod_inspetoria_ts_msg': 'Unidade+n%E3o+informada.',
            'cod_tipo_ciclo': '1',
            'num_ciclo_ts': '714',
            'txt_nome_ref_mesano': 'M%EAs%2FAno',
            'txt_label_tipo_ciclo': 'M%EAs%2FAno',
            'incTemEmpresa': 'S',
            'incTemLotacao': 'S',
            'incTemCC': 'N',
            'incAuxValidaContrato': 'N',
            'incTipoAssociado': 'T',
            'incLabelAssociado': 'Titular',
            'ind_tipo_relatorio': 'N',
            'ind_ordenacao_contrato': 'C',
            'ind_ordenacao_associado': 'C',
            'ind_quebra_lotacao': 'E',
            'ind_formato_saida': 'T',
            'txt_nome_label_sucursal': 'Filial',
            'txt_nome_label_inspetoria': 'Unidade',
            'cod_identificacao_ts': '39951592',
            'cod_tipo_usuario': '2',
            'num_contrato_acesso_externo': '59943115',
            'ind_ano_demonstrativo': 'N',
            'p_versao': 'Revision%3A+v12.1.3515',
        }
        params = {
            'PT': 'Demonstrativo Analítico Faturamento',
            'txt_cod_operadora': 'Unimed Seguros Saude SA',
            'txt_nome_label_sucursal': 'Filial',
            'txt_cod_sucursal': 'FILIAL SÃO PAULO',
            'txt_nome_label_inspetoria': 'Unidade',
            'txt_cod_inspetoria_ts': 'MATRIZ',
            'txt_cod_tipo_ciclo': 'Prêmio',
            'txt_num_ciclo_ts': competence.strftime('%m/%Y'),
            'nom_tipo_ciclo': 'Prêmio',
        }
        url = 'https://topsaude.segurosunimed.com.br/fat/asp/fat1001b.asp?'
        url += parse.urlencode(params, encoding='latin1', quote_via=parse.quote, safe='')

        response = self.session.post(url, data=payload)

        file_ref = re.findall(r"AbreDownload \('(.*)',", response.text)[0]

        return file_ref


    def __get_file_url(self, file_ref: str) -> str:
        params = {
            'PT': 'Demonstrativo%20Anal%EDtico%20Faturamento',
            'sNomeArquivo': file_ref,
            'sMsgRetorno': '',
        }
        url = 'https://topsaude.segurosunimed.com.br/cli/asp/AtivaDownload.asp'
        response = self.session.post(url, params=params)

        file_url = re.findall(r"document.form01.action = '(.*)';", response.text)[0]
        file_url = file_url.strip('../../')
        file_url = 'https://topsaude.segurosunimed.com.br/' + file_url

        return file_url


    def __get_file_content(self, file_url: str) -> str:
        response = self.session.get(file_url)

        return response.content


    def get_premio(self, competence: datetime) -> str:
        file_ref = self.__request_file(competence)
        file_url = self.__get_file_url(file_ref)
        content = self.__get_file_content(file_url)

        return content