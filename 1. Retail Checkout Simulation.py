
def main():
    prices = []  # List to store item prices
    
    print("Welcome to the Retail Checkout System")
    print("Enter item prices. Type 0 to finish.\n")

    while True:
        price = float(input("Enter item price: $"))

        # Stop loop if user enters 0
        if price == 0:
            break

        # Validate negative input
        if price < 0:
            print("Price cannot be negative. Try again.\n")
        else:
            prices.append(price) 

    # Calculations
    number_of_items = len(prices)

    if number_of_items > 0:
        total = sum(prices)
        average = total / number_of_items
    else:
        total = 0
        average = 0

    # Output results
    print("\n----- Receipt Summary -----")
    print(f"Number of items: {number_of_items}")
    print(f"Total purchase amount: ${total:.2f}")
    print(f"Average item cost: ${average:.2f}")


# Run the program
main()
