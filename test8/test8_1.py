class Cat:
    name = 'saimon'

    def __init__(self):
        self.name = 'barsik'

    def get_name(self):
        return self.name

cat1=Cat()
print(cat1.get_name())
