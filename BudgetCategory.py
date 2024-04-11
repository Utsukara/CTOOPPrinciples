class budget_category:
    def __init__(self, category_name: str, allocated_budget: float):
        self._category_name = category_name
        self._allocated_budget = allocated_budget
        self._expenses = []
        self._remaining_budget = allocated_budget

    # Getters & Setters 
    def get_category_name(self):
        return self._category_name

    def set_category_name(self, new_name: str):
        self._category_name = new_name

    def get_allocated_budget(self) -> float:
        return self._allocated_budget

    def set_allocated_budget(self, new_budget: float):
        if new_budget > 0:
            self._allocated_budget = new_budget
            self._remaining_budget = new_budget  # Update remaining budget
        else:
            print("Budget cannot be negative or zero.")

    # Add Expense
    def add_expense(self, amount: float):
        if amount <= 0:
            print("Expense amount must be greater than zero.")
        elif amount <= self._remaining_budget:
            self._expenses.append(amount)
            self._remaining_budget -= amount
            print(f"Budget remaining: ${self._remaining_budget:.2f}")
        else:
            print("Insufficient budget for this expense.")

    # Display Summary
    def display_category_summary(self):
        print(f"\nCategory: {self._category_name}")
        print(f"Allocated Budget: ${self._allocated_budget:.2f}")
        print(f"Remaining Budget: ${self._remaining_budget:.2f}")
        if self._expenses:  # Show expenses if they exist
            print("Expenses:")
            for expense in self._expenses:
                print(f"- ${expense:.2f}")