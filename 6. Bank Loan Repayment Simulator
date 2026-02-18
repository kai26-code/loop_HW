def simulate_loan(balance, annual_rate, monthly_payment):
    """Simulate loan repayment and return number of months needed."""
    
    monthly_rate = annual_rate / 100 / 12  # Convert annual % to monthly decimal
    months = 0

    # Prevent infinite loop if payment is too small
    if monthly_payment <= balance * monthly_rate:
        return -1  # Payment too low to ever pay off loan

    while balance > 0:
        # Add monthly interest
        interest = balance * monthly_rate
        balance += interest

        # Subtract monthly payment
        balance -= monthly_payment

        months += 1

    return months


def main():
    print("===== Loan Repayment Simulator =====\n")

    loan_amount = float(input("Enter loan amount: $"))
    interest_rate = float(input("Enter annual interest rate (%): "))
    monthly_payment = float(input("Enter monthly payment: $"))

    months_needed = simulate_loan(loan_amount, interest_rate, monthly_payment)

    if months_needed == -1:
        print("\nMonthly payment is too low to ever pay off this loan.")
    else:
        print(f"\nLoan will be paid off in {months_needed} months.")


# Run program
main()