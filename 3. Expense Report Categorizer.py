def main():
    # Expense data
    expenses = {
        "Travel": [500, 200],
        "Meals": [40, 60, 30],
        "Supplies": [100]
    }

    grand_total = 0

    print("====== Expense Summary Report ======\n")

    # Outer loop: go through each category
    for category in expenses:
        category_total = 0

        # Inner loop: add expenses within that category
        for amount in expenses[category]:
            category_total += amount

        grand_total += category_total

        print(f"{category} Total: ${category_total:.2f}")

    print("\n------------------------------------")
    print(f"Grand Total: ${grand_total:.2f}")


# Run the program
main()