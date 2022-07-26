class Cat:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


cat1 = Cat('Barsik')
name = cat1.name
print(name)

#cat.name() = 'Saimon'