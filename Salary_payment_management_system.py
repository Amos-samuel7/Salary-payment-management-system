salary_payments = []

def record_payment():
    employee = input("Enter employee name: ")
    amount = float(input("Enter salary amount: "))
    salary_payments.append({
        "employee": employee,
        "amount": amount
    })
    print("Salary payment recorded")

def view_payments():
    if not salary_payments:
        print("No salary payments found")
    else:
        for s in salary_payments:
            print("Employee:", s["employee"], "| Amount:", s["amount"])

def main():
    while True:
        print("1. Record Salary Payment")
        print("2. View Salary Payments")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            record_payment()
        elif choice == "2":
            view_payments()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

main()
