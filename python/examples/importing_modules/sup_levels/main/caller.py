import os, sys
new_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(new_path)

import callee
callee.say_hello()