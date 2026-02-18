def main():
    # Example projected revenues (in thousands)
    revenues = [3, 5, 8, 10, 12]

    print("===== Startup Revenue Projection =====\n")

    # Loop through revenue data
    for year in range(len(revenues)):
        bar = "#" * revenues[year]  # String multiplication
        print(f"Year {year + 1}: {bar}")


# Run program
main() 
