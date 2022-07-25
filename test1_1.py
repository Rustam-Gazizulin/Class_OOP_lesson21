class Sample:

    def __init__(self, value=1):
        self.value = value

    def foo(self):
        return self.value


sample = Sample(2)
print(sample.foo())
