def show_messages(short_messages):
    """Prints a list of short messages from a list"""
    for short_message in short_messages:
        print(short_message)

def send_messages(short_messages, sent_messages):
    """Send short messages"""
    while short_messages:
        current_message = short_messages.pop()
        print(f"Sending message: '{current_message}'.")
        sent_messages.append(current_message)

short_messages = [
                'Hello there!',
                'Luke, I am your father.',
                'English motherfucker, do you speak it?'
                ]
sent_messages = []

send_messages(short_messages, sent_messages)
show_messages(short_messages)

print(short_messages)
print(sent_messages)