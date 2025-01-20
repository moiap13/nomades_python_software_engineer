import sys, os
wanted_path: str = os.path.join(os.path.dirname(os.path.dirname(__file__)), "modules")
sys.path.append(wanted_path)

import callee
callee.say_hello()