class Host:
    def __init__(self, name):
        self._name = name

    def set_name(self, new_name):
        self._name = new_name


user1 = Host('Jhon')
print(user1._name)
user1.set_name('Artur')
print(user1._name)
