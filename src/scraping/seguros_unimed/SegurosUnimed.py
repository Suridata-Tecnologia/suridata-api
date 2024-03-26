from requests import Session
from html import unescape
from bs4 import BeautifulSoup as BS
import re

from .Sinistralidade import Sinistralidade
from .Sinistro import Sinistro
from .Premio import Premio


class SegurosUnimed:
    def __init__(self, username: str, password: str ) -> None:
        self.access_key: str = None
        self.session: Session = Session()
        self.contract: dict = {}

        self.__auth(username, password)

        self.premio: Premio = Premio(self.session)
        self.sinistro: Sinistro = Sinistro(self.session, self.contract, self.access_key)
        self.sinistralidade: Sinistralidade = Sinistralidade(self.session, self.contract)


    def __setup_headers(self) -> None:
        self.session.headers.update({'Content-Type': 'application/x-www-form-urlencoded'})


    def __add_long_session_cookie(self) -> None:
        self.session.get('https://topsaude.segurosunimed.com.br/TSNMVC/TSNMVC/Account/Login')


    def __user_authentication(self, username: str, password: str) -> None:
        url = "https://topsaude.segurosunimed.com.br/TSNMVC/Account/AutenticarUsuario?returnUrl="
        payload = { 'usuario': username, 'senha': password }

        response = self.session.post(url, data=payload)

        has_error_message = re.search(r'(?<=notificacoes.erro\()(.*)(?=\);)', response.text)
        if has_error_message:
            error_message = unescape(has_error_message.group(1)).strip("'")

            raise Exception(error_message)


    def __set_access_key(self) -> None:
        response = self.session.get("https://topsaude.segurosunimed.com.br/TSNMVC/TSNMVC/Home/AreaLogada")

        access_key = re.search(r"(?<=var chave = encodeURIComponent\(')(.*)(?='\);)", response.text).group(0)

        self.access_key = access_key


    def __add_logged_user_cookie(self) -> None:
        logged_user = self.access_key.split('[TD]')[3]

        self.session.cookies.set('usuarioLogadoRastreamento', logged_user)


    def __create_session(self) -> None:
        url = f"https://topsaude.segurosunimed.com.br/ace/mvcToAsp.asp"
        params = {
            'criar_sessao': 'S',
            'chaveAcesso': self.access_key
        }
        self.session.get(url, params=params)


    def __add_binding_cookies(self) -> None:
        url = 'https://topsaude.segurosunimed.com.br/ace/mvcToAsp.asp'
        params = {
            '../../ace/ace003d.asp?vinculacao': 'beneficiario$$$p=',
            'PT': 'Mensagens',
            'pm': '40',
            'pcf': 'ATB0083', #verificar outras empresas
            'css': 'unimed.css',
            'codIdentificacaoTs': '39951592', #verificar outras empresas
            'tipo_usuario': '2',
            'chaveAcesso': self.access_key,
        }
        self.session.get(url, params=params)

        url = 'https://topsaude.segurosunimed.com.br/gen/css/css002.css'
        self.session.get(url)

        url = 'https://topsaude.segurosunimed.com.br/ace/ace003d.asp'
        params = {
            'vinculacao': 'beneficiario',
            'p': '',
            'PT': 'Mensagens',
            'pm': '40',
            'pcf': 'ATB0083',
            'css': 'unimed.css',
            'codIdentificacaoTs': '39951592',
            'tipo_usuario': '2',
            'chaveAcesso': self.access_key,
        }
        self.session.get(url, params=params)


    def __set_contract(self) -> None:
        url = 'https://topsaude.segurosunimed.com.br/ger/asp/ger0029a.asp'
        params = {
            'p': '',
            'PT': 'Sinistralidade por Grupo',
            'pm': '91',
            'pcf': 'GER13.12',
            'pprf': 'ESTIPULANTE_EMPRESA',
            'PPRM': 'S,S,S,S,N,N',
            'tipoFuncao': 'A',
            'css': 'unimed.css',
            'codIdentificacaoTs': '39951592',
            'tipo_usuario': '2',
            'chaveAcesso': self.access_key,
        }
        response = self.session.get(url, params=params)

        soup = BS(response.text, 'html.parser')

        self.contract = {
            'code': soup.select_one('#cod_grupo_empresa')['value'],
            'name': soup.select_one('#nome_grupo_empresa')['value'],
        }


    def __auth(self, username: str, password: str) -> None:
        self.__setup_headers()
        self.__add_long_session_cookie()
        self.__user_authentication(username, password)
        self.__set_access_key()
        self.__add_logged_user_cookie()
        self.__create_session()
        self.__add_binding_cookies()
        self.__set_contract()