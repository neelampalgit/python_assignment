def track_expenses():
    expenses = []
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter expense name: ")
            amount = float(input("Enter amount: "))
            expenses.append({"name": name, "amount": amount})
        elif choice == 2:
            print("Expenses:")
            for expense in expenses:
                print(f"{expense['name']}: ${expense['amount']}")
        elif choice == 3:
            break
        else:
            print("Invalid choice.")

track_expenses()
