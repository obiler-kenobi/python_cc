from pathlib import Path
import json

def get_stored_user_informations(path):
    """Get stored information of the user if available"""
    if path.exists():
        contents = path.read_text()
        user_informations = json.loads(contents)
        return user_informations
    else:
        return None
    
def get_new_user_informations(path):
    """Prompt user to get information"""
    user_informations = {}
    user_informations["username"] = input("What is your name? ")
    user_informations["email"] = input("What is your email address? ")
    user_informations["age"] = input("How old are you? ")
    contents = json.dumps(user_informations)
    path.write_text(contents)
    return user_informations

    # Book solution
    # username = input("What is your name? ")
    # game = input("What's your favorite game? ")
    # animal = input("What's your favorite animal? ")

    # user_dict = {
    #     'username': username,
    #     'game': game,
    #     'animal': animal,
    # }

def greet_user():
    path = Path('user_information.json')
    user_informations = get_stored_user_informations(path)
    if user_informations:
        print(f"Hi user. I remember you! You have the following details:")
        for key, value in user_informations.items():
            print(f"{key.title()}: {value}")
            
    # Book solution
    # print(f"Welcome back, {user_dict['username']}!")
    # print(f"Hope you've been playing some {user_dict['game']}. ")
    # print(f"Have you seen a {user_dict['animal']} recently?")
    else:
        user_informations = get_new_user_informations(path)
        print(f"Hi user. I'll remember you and your following details:")
        for key, value in user_informations.items():
            print(f"{key.title()}: {value}")

greet_user()