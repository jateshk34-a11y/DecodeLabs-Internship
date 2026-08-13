print("=" * 40)
print("        EXPENSE TRACKER")
print("=" * 40)

num_expenses = int(input("How many expenses do you want to enter? "))

total_spent = 0

for i in range(1, num_expenses + 1):
    expense = float(input(f"Enter expense {i}: Rs. "))
    total_spent += expense

print("\n" + "=" * 40)
print(f"Total Expenses : {num_expenses}")
print(f"Total Spent    : Rs. {total_spent:.2f}")
print("=" * 40)

print("\nThank you for using Expense Tracker!")