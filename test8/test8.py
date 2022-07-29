class Cat:
    color = 'grey'
    breed = 'bengal'
    name = 'saimon'
    total_snack = 0

    def __init__(self, name):
        self.name = name

    def add_snack(self):
        Cat.total_snack += 1

    def get_snack(self):
        return Cat.total_snack

    @classmethod
    def get_default(cls):
        return cls.name

Cat.color = 'red'

# print(Cat.breed)
# print(Cat.name)
print(Cat.color)
cat1 = Cat('barsik')
cat2 = Cat('simon')
cat2.add_snack()
cat1.add_snack()
print(cat1.color)
# print(cat1.breed)
# print(cat1.name)
print(cat2.total_snack)
print(Cat.total_snack)
print(Cat.get_default())
