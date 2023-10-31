import sys
import os

# Add the sub_directory to the module search path
sup_directory = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(sup_directory)

import callee

callee.say_hello()