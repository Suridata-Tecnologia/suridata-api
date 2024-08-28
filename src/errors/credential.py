class DuplicatedCredential(Exception):
    def __init__(self, msg='Duplicated credential ', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)