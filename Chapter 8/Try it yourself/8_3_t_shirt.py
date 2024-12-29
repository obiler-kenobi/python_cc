def make_shirt(shirt_text, shirt_size='medium'):
    """Make a t-shirt"""
    print(f"\nYou bought a {shirt_size.title()} sized shirt with text: {shirt_text} printed on it.")
    
make_shirt('Hello World!','small')
make_shirt(shirt_size='large', shirt_text="Henlo World!!")
make_shirt('Hanlooo!!')
    