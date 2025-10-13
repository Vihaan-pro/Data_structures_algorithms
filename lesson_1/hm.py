class Laptop:
    brand = ""
    ram = 0
    storage = 0

    def power_on(self):
        print(self.brand ,"laptop is powering on.")

    def specs(self):
        print(f"Brand: {self.brand}, RAM: {self.ram}GB, Storage: {self.storage}GB")


class Book:
    title = ""
    author = ""
    pages = 0

    def read(self):
        print(f"Reading '{self.title}' by {self.author}.")

    def info(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}")


# Creating Laptop objects
laptop1 = Laptop()
laptop1.brand = "Dell"
laptop1.ram = 8
laptop1.storage = 512

laptop2 = Laptop()
laptop2.brand = "HP"
laptop2.ram = 16
laptop2.storage = 1024

laptop3 = Laptop()
laptop3.brand = "Apple"
laptop3.ram = 32
laptop3.storage = 2048

laptop1.power_on()
laptop2.specs()
laptop3.specs()

# Creating Book objects
book1 = Book()
book1.title = "1984"
book1.author = "George Orwell"
book1.pages = 328

book2 = Book()
book2.title = "To Kill a Mockingbird"
book2.author = "Harper Lee"
book2.pages = 281

book3 = Book()
book3.title = "The Great Gatsby"
book3.author = "F. Scott Fitzgerald"
book3.pages = 180

book1.read()
book2.info()
book3.info()