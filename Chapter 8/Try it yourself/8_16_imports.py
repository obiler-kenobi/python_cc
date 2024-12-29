# import module_name
import Modules.printing_functions

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

Modules.printing_functions.print_models(unprinted_designs,completed_models)
Modules.printing_functions.show_completed_models(completed_models)

# from module_name import function_name
from Modules.printing_functions import print_models, show_completed_models

unprinted_designs = ['phone case 1', 'robot pendant 1', 'dodecahedron 1']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

# from module_name import function_name as fn
from Modules.printing_functions import (print_models as pm,
                                        show_completed_models as scm)

unprinted_designs = ['phone case 2', 'robot pendant 2', 'dodecahedron 2']
completed_models = []

pm(unprinted_designs,completed_models)
scm(completed_models)

# import module_name as mn
import Modules.printing_functions as pf

unprinted_designs = ['phone case 3', 'robot pendant 3', 'dodecahedron 3']
completed_models = []

pf.print_models(unprinted_designs,completed_models)
pf.show_completed_models(completed_models)

# from module_name import *
from Modules.printing_functions import *

unprinted_designs = ['phone case 4', 'robot pendant 4', 'dodecahedron 4']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)