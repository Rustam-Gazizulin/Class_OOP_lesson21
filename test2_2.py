class SomeClass:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def print(self):
        print(self._concat())

    def _concat(self):
        return f'{self.var1} - {self.var2}'


object1 = SomeClass(var1='hello', var2='World')
object1.print()
