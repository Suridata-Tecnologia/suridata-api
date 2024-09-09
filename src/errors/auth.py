class UserNotFound(Exception):
    def __init__(self, msg='User not found', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class WrongPassword(Exception):
    def __init__(self, msg='Password incorrect', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)