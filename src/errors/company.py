class CompanyNotFound(Exception):
    def __init__(self, msg='Company not found', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)