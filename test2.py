class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def change_password(self, old_password, new_password):  # public method - можно использовать с наружи класса, внутри класса, наследовать потомкам.
        self._password_is_correct(old_password)
        self.__password_is_valid(new_password)
        self._was_password_used(new_password)
        pass

    def _password_is_correct(self, old_password):  # protected method - недоступны снаружи класса, но доступны для потомков и внутри класса
        pass

    def __password_is_valid(self, new_password):  # private method - доступны только внутри класса
        pass

    def _was_password_used(self, new_password):
        pass



user1 = User('Jhon', '12345')
