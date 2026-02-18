def main():
    print("===== Business Growth Projection =====\n")

    initial_revenue = float(input("Enter initial revenue: $"))
    growth_rate = float(input("Enter annual growth rate (%): "))

    growth_decimal = growth_rate / 100  # Convert percent to decimal
    revenue = initial_revenue

    print("\nYear | Projected Revenue")
    print("-------------------------")

    # Loop through 10 years
    for year in range(1, 11):
        revenue = revenue * (1 + growth_decimal)
        print(f"{year:>4} | ${revenue:,.2f}")


# Run program
main()