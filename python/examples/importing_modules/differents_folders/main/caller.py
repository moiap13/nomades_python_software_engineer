import sys, os

parent_folder = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(parent_folder, "modules"))

import callee

callee.say_hello()