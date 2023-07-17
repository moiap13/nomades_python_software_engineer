import sys
import os

# Add the sub_directory to the module search path
sub_directory = os.path.join(os.path.dirname(__file__), '../modules')
sys.path.append(sub_directory)


n=-2
if n > 0:
    import callee
    callee.say_hello()