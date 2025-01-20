import sys
import os

wanted_path: str = os.path.dirname(os.path.dirname(__file__))
sys.path.append(wanted_path)

print(sys.path)

import callee

callee.say_hello()

