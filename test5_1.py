class StoreItem:
    def calculate(self, count):
        self.count = count
        return self._calculate_tax(count) + (count * 10)

    def _calculate_tax(self, count):
        return self.count * 0.1


class StoreItemWorld(StoreItem):
    def _calculate_tax(self, count):
        return self.count * 0.5


store1 = StoreItemWorld()
print(store1.calculate(10))
store2 = StoreItem()
print(store2.calculate(10))
