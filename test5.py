class Book:
    def __init__(self, name, page, content, author):
        self.name = name
        self.page = page
        self.content = content
        self.author = author


class Ebook(Book):
    def __init__(self, name, page, content, author, links):
        super().__init__(name, page, content, author)
        self.links = links


book1 = Book('Phyton', 325, 'code', 'Jhon')
book2 = Ebook('Phyton', 325, 'code', 'Jhon', ['http://library/ebook.com'])

print(book2.author)
