import random

def calculate_total_value(portfolio):
    """Calculate and return total portfolio value."""
    total = 0

    for stock in portfolio:
        shares = portfolio[stock]["shares"]
        price = portfolio[stock]["price"]
        total += shares * price

    return total


def main():
    portfolio = {
        "AAPL": {"shares": 10, "price": 170},
        "TSLA": {"shares": 4, "price": 250},
        "AMZN": {"shares": 2, "price": 130} 
    }

    print("====== Initial Portfolio Value ======")
    total_value = calculate_total_value(portfolio)
    print(f"Total Portfolio Value: ${total_value:.2f}\n")

    print("====== Simulated 5-Day Market Changes ======\n")

    # Simulate 5 days
    for day in range(1, 6):
        print(f"Day {day}:")

        # Update each stock price
        for stock in portfolio:
            change_percent = random.uniform(-0.05, 0.05)
            portfolio[stock]["price"] *= (1 + change_percent)

            print(f"  {stock} new price: ${portfolio[stock]['price']:.2f}")

        # Recalculate total portfolio value
        total_value = calculate_total_value(portfolio)
        print(f"  Total Portfolio Value: ${total_value:.2f}\n")


# Run the program
main()