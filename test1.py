class House:
    def __init__(self, number, color, owner):
        self.number = number
        self.color = color
        self.owner = owner

    def get_owner(self, surname):
        return self.owner + '-' + surname


house1 = House(10, 'red', 'Jhon')
house2 = House(11, 'green', 'Maria')
house3 = House(12, 'black', 'Ivan')

print(house1.owner)
owner_name = house1.get_owner('ivanov')
print(owner_name)
print(house2.color)
print(house3.number)
