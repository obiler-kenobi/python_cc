def make_car(manufacturer, model_name, **car_information):
    """Buid a dictionary about a car and its informations"""
    car_information['manufacturer'] = manufacturer
    car_information['model'] = model_name
    return car_information

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

car = make_car('tesla', 'model 3', recharge_time=3, type='electric')
print(car)


# book solution to sort the key-value pairs properly
def make_car(manufacturer, model, **options):
    """Make a dictionary representing a car."""
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
        }
    for option, value in options.items():
        car_dict[option] = value

    return car_dict

my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)

my_old_accord = make_car('honda', 'accord', year=1991, color='white',
        headlights='popup')
print(my_old_accord)

# NOTE: make use of this example in projects