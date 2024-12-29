"""This practice code shows how importing a module works"""

import Modules.printing_functions

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

Modules.printing_functions.print_models(unprinted_designs,completed_models)
Modules.printing_functions.show_completed_models(completed_models)
