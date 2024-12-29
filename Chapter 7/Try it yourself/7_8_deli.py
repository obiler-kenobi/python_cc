sandwich_orders = ['grilled cheese', 'club', 'egg', 'tuna', 'pastrami',
                    'cuban', 'roast beef']
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()

    print(f"\nI made your {current_order} sandwich! Enjoy!")
    finished_sandwiches.append(current_order)

print("\n--- Finished Sandwiches ---")
for sandwich in finished_sandwiches:
    print(sandwich)