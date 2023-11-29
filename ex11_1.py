class book_publication:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f"Publication Name: {self.name}")


class Book(book_publication):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages

    def print_info(self):
        super().print_info()
        print(f"Author: {self.author}")
        print(f"Page Count: {self.pages}")


class Magazine(book_publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor

    def print_info(self):
        super().print_info()
        print(f"Chief Editor: {self.editor}")


donald_duck = Magazine(name="Donald Duck", editor="Aki Hyyppä")
compartment_no_6 = Book(name="Compartment No. 6", author="Rosa Liksom", pages=192)
donald_duck.print_info()
print("\n")
compartment_no_6.print_info()
