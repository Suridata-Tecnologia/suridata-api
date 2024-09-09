class UserDuplicated(Exception):
    def __init__(self, msg='Duplicated user', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)

class UserNotFound(Exception):
    def __init__(self, msg='User not found', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)