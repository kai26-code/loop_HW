def main():
    warehouses = [
        {"name": "Warehouse A", "inventory": {"apples": 100, "bananas": 150}},
        {"name": "Warehouse B", "inventory": {"apples": 200, "bananas": 100}}
    ]

    total_inventory = {}

    # Outer loop: go through each warehouse
    for warehouse in warehouses:
        print(f"Checking {warehouse['name']}")

        # Inner loop: go through each product in that warehouse
        for product in warehouse["inventory"]:
            quantity = warehouse["inventory"][product]

            if product in total_inventory:
                total_inventory[product] += quantity
            else:
                total_inventory[product] = quantity

    print("\n===== Total Supply Chain Inventory =====\n")

    for product in total_inventory:
        print(f"{product.title()}: {total_inventory[product]} units")


# Run program
main()