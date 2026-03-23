class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show(self):
        print(self.title, "-", self.author)

b1 = Book("Python", "Mit")
b2 = Book("Java", "Raj")

b1.show()
b2.show()