import sys
import os
print(sys.path)

calle_path = "/Users/antonio/Documents/Depannit/Nomades/2023/Python/tmp/nomades_python_software_engineer/python/exemples/importing_modules/sup_levels"

# Add the sub_directory to the module search path
#sup_directory = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(calle_path)
print(sys.path)

import callee

callee.say_hello()