def main():
    # Fake survey data (students can modify this list)
    responses = ["coffee", "tea", "coffee", "soda"]

    counts = {}  # Dictionary to store product counts

    # Count responses using a for loop
    for item in responses:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    total_responses = len(responses)

    print("Market Share Summary\n")

    # Calculate and print percentages
    for product in counts:
        percentage = (counts[product] / total_responses) * 100
        print(f"{product}: {percentage:.0f}%")

# Run the program
main() 