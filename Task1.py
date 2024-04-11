from BudgetCategory import budget_category


def main():
    #test()
    ui()


def test():
    # Create a budget category
    category = budget_category("Food", 1000)

    # Add expenses
    category.add_expense(150)
    category.add_expense(200)
    category.add_expense(300)

    # Display category summary
    category.display_category_summary()

    # Update category name
    category.set_category_name("Groceries")
    print(f"Category name: {category.get_category_name()}")

    # Update allocated budget
    category.set_allocated_budget(2000)
    print(f"Allocated budget: {category.get_allocated_budget()}")

    # Display category summary
    category.display_category_summary()

    # Test negative budget
    category.set_allocated_budget(-500)

    # Test zero budget
    category.set_allocated_budget(0)

    # Test negative expense
    category.add_expense(-100)

    # Test insufficient budget
    category.add_expense(2000)



def ui():
    # Create a budget category
    budget_categories = []

    while True:
        print("\nBudget Category Menu")
        print("1. Create a Budget Category")
        print("2. Add Expense")
        print("3. Display Category Summary")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            category_name = input("Enter the category name: ")
            if category_name in budget_categories:
                print("Category already exists.")
                continue
            allocated_budget = float(input("Enter the allocated budget: "))
            if allocated_budget <= 0:
                print("Budget cannot be negative or zero.")
                continue
            category = budget_category(category_name, allocated_budget)
            budget_categories.append(category)  # Add the category object
            print(f"Budget category '{category_name}' created.")

        elif choice == "2":
            category_name = input("Enter the category name: ")
            amount = float(input("Enter the expense amount: "))
            category = find_category(budget_categories, category_name)
            if category:
                category.add_expense(amount)
            else:
                print("Category does not exist.")

        elif choice == "3":
            category_name = input("Enter the category name: ")
            category = find_category(budget_categories, category_name)
            if category:
                category.display_category_summary()
            else:
                print("Category does not exist.")

        elif choice == "4":
            print("Exiting program.")
            


def find_category(categories, name):
    for category in categories:
        if category.get_category_name() == name:
            return category
    return None



if __name__ == "__main__":
    main()
