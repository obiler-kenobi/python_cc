sandwich_orders = ['grilled cheese', 'pastrami', 'egg', 'tuna', 'pastrami',
                    'cuban', 'pastrami']
finished_sandwiches = []

print("We're sorry, but we run out of pastrami.")

# book solution
# while 'pastrami' in sandich_orders:
#   sandwich_orders.remove('pastrami')

# while sandwich_orders:
#         current_order = sandwich_orders.pop()
#         print(f"\nI made your {current_order} sandwich! Enjoy!")
#         finished_sandwiches.append(current_order)

# print("\n--- Finished Sandwiches ---")
# for sandwich in finished_sandwiches:
#     print(sandwich)

while sandwich_orders:
    if 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    else:
        current_order = sandwich_orders.pop()
        print(f"\nI made your {current_order} sandwich! Enjoy!")
        finished_sandwiches.append(current_order)

print("\n--- Finished Sandwiches ---")
for sandwich in finished_sandwiches:
    print(sandwich)