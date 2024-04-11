import random

class Product:
    all_ids = set()  # Track all generated IDs

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.generate_unique_id()

    def generate_unique_id(self):
        """Generates a unique ID and adds it to the tracking set."""
        while True:
            potential_id = random.randint(0, 1000000)
            if potential_id not in Product.all_ids:
                self.id = potential_id
                Product.all_ids.add(self.id)
                break

    def __str__(self):
        return f"{self.name}: {self.price}"

    def __repr__(self):
        return f"Product:(\nName: {self.name}\nPrice: {self.price}\nProduct ID: {self.id})"
    


class Book(Product):
    def __init__(self, name, price, author):
        super().__init__(name, price)
        self.author = author

    def __str__(self):
        return f"{self.name} by {self.author}: {self.price}"

    def __repr__(self):
        return f"Book:(\nName: {self.name}\nPrice: {self.price}\nAuthor: {self.author}\nProduct ID: {self.id})"
    


class Electronic(Product):
    def __init__(self, name, price, manufacturer):
        super().__init__(name, price)
        self.manufacturer = manufacturer
        self.specs = "None"
        self.warranty = 0

    def __str__(self):
        return f"{self.name} by {self.manufacturer}: {self.price}"
        
    def __repr__(self):
        return f"Electronic:(\nName: {self.name}\nPrice: {self.price}\nManufacturer: {self.manufacturer}\nProduct ID: {self.id}"



class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size
        self.color = "None"
        self.material = "None"

    def __str__(self):
        return f"{self.name} in size {self.size}: {self.price}"
        
    def __repr__(self):
        return f"Clothing:(\nName: {self.name}\nPrice: {self.price}\nSize: {self.size}\nProduct ID: {self.id}"




class Food(Product):
    def __init__(self, name, price, expiration_date):
        super().__init__(name, price)
        self.expiration_date = expiration_date
        self.calories = 0
        self.ingredients = "None"

    def __str__(self):
        return f"{self.name} expiring on {self.expiration_date}: {self.price}"
            
    def __repr__(self):
         return f"Food:(\nName: {self.name}\nPrice: {self.price}\nExpiration Date: {self.expiration_date}\nProduct ID: {self.id}"