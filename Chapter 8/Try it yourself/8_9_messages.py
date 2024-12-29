def show_messages(short_messages):
    """Prints a list of short messages from a list"""
    for short_message in short_messages:
        print(short_message)

short_messages = [
                'Hello there!',
                'Luke, I am your father.',
                'English motherfucker, do you speak it?'
                ]

show_messages(short_messages)