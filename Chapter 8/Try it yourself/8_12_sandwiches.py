def make_sandwich(*stuffings):
    """Make me a sandwich"""
    print("Hello, you ordered a sandwich with the followings stuffings:")
    for stuffing in stuffings:
        print(f"- {stuffing}")

make_sandwich('ham')
make_sandwich('cheese', 'bacon')
make_sandwich('tomato', 'lettuce', 'brisket')