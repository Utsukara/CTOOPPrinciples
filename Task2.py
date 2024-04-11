from Product import Product, Book, Electronic, Clothing, Food

def main():
    #test()
    products = product_adder()
    customer_ui(products)


def test():
    # Create a product
    product = Product("Shirt", 20)
    print(product)
    print(repr(product))

    # Create a book
    book = Book("Harry Potter", 15, "J.K. Rowling")
    print(book)
    print(repr(book))

    # Create an electronic
    electronic = Electronic("iPhone", 1000, "Apple")
    print(electronic)
    print(repr(electronic))

    # Create a clothing
    clothing = Clothing("Jeans", 50, "M")
    print(clothing)
    print(repr(clothing))

    # Create a food
    food = Food("Apple", 1, "01/01/2022")
    print(food)
    print(repr(food))


def product_adder():
    products = []

    while True:
        print("\nProduct Manager:")
        print("1. Add Product")
        print("2. Add Book")
        print("3. Add Electronic")
        print("4. Add Clothing")
        print("5. Add Food")
        print("6. Display Products")
        print("7. Display Product Details")
        print("8. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter the product name: ")
            price = float(input("Enter the product price: "))
            product = Product(name, price)
            products.append(product)
            print("Product added successfully!")

        elif choice == "2":
            name = input("Enter the book name: ")
            price = float(input("Enter the book price: "))
            author = input("Enter the book author: ")
            book = Book(name, price, author)
            products.append(book)
            print("Book added successfully!")

        elif choice == "3":
            name = input("Enter the electronic name: ")
            price = float(input("Enter the electronic price: "))
            brand = input("Enter the electronic brand: ")
            electronic = Electronic(name, price, brand)
            products.append(electronic)
            print("Electronic added successfully!")

        elif choice == "4":
            name = input("Enter the clothing name: ")
            price = float(input("Enter the clothing price: "))
            size = input("Enter the clothing size: ")
            clothing = Clothing(name, price, size)
            products.append(clothing)
            print("Clothing added successfully!")

        elif choice == "5":
            name = input("Enter the food name: ")
            price = float(input("Enter the food price: "))
            expiry_date = input("Enter the food expiry date (MM/DD/YYYY): ")
            food = Food(name, price, expiry_date)
            products.append(food)
            print("Food added successfully!")

        elif choice == "6":
            print("\nProducts:")
            for product in products:
                print(product)

        elif choice == "7":
            index = int(input("Enter the index of the product: "))
            if index >= 0 and index < len(products):
                print(products[index])
            else:
                print("Invalid index!")

        elif choice == "8":
            print("Exiting...")
            return products
            break

        else:
            print("Invalid choice! Please try again.")

def customer_ui(products):
    cart = []
    total = 0

    while True:
        print("\nCustomer Menu")
        print("1. Display Products")
        print("2. Display Product Details")
        print("3. Add Product to Cart")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("\nProducts:")
            for product in products:
                print(product)

        elif choice == "2":
            index = int(input("Enter the index of the product: "))
            if index >= 0 and index < len(products):
                print(products[index])
            else:
                print("Invalid index!")

        elif choice == "3":
            product_name = input("Enter the product name: ")
            for product in products:
                if product.name == product_name:
                    cart.append(product)
                    total += product.price
                    print("Product added to cart!")
                    break
                else:
                    print("Product not found!")

        elif choice == "4":
            print("\nCart:")
            for product in cart:
                print(product)
            print(f"Total: {total}")
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()