class Pole:
    def __init__(self, name, page, content):
        self.name = name
        self.page = page
        self.content = content


class Book(Pole):
    def __init__(self, name, page, content, author):
        super().__init__(name, page, content)
        self.author = author


class Magazine(Pole):
    def __init__(self, name, page, content):
        super().__init__(name, page, content)


book1 = Book('Jhon', 330, 'code', 'Mary')
magazine1 = Magazine('Phyton', 110, 'World')
print(book1.name)
print(magazine1.page)


