def calculate_commission(sales_amount):
    """Return 10% commission based on sales amount."""
    return sales_amount * 0.10


def main():
    sales = {
        "Alice": 5000,
        "Bob": 7000,
        "Carol": 3000
    }

    commissions = {}

    # Calculate commission for each employee
    for employee in sales:
        commission = calculate_commission(sales[employee])
        commissions[employee] = commission

    # Sort employees by commission (highest first)
    ranked = sorted(commissions.items(), key=lambda item: item[1], reverse=True)

    print("====== Commission Leaderboard ======\n")

    for rank, (employee, commission) in enumerate(ranked, start=1):
        print(f"{rank}. {employee} - Commission: ${commission:.2f}")


# Run the program
main()