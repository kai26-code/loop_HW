def main():
    customers = {
        "Alice": 750,
        "Bob": 3200,
        "Carol": 5400,
        "David": 1200,
        "Emma": 6800
    }

    # Dictionary to track tier counts
    tier_counts = {
        "Bronze": 0,
        "Silver": 0,
        "Gold": 0
    }

    # Loop through customers and assign tiers
    for customer in customers:
        total_spent = customers[customer]

        if total_spent < 1000:
            tier = "Bronze"
        elif 1000 <= total_spent <= 4999:
            tier = "Silver"
        else:
            tier = "Gold"

        tier_counts[tier] += 1

        print(f"{customer} → {tier} Tier")

    # Print summary
    print("\n===== Loyalty Tier Summary =====\n")

    for tier in tier_counts:
        print(f"{tier}: {tier_counts[tier]} customers")


# Run program
main()