import sys
import os


# Add the sub_directory to the module search path
sub_directory = os.path.join(os.path.dirname(__file__), '../modules')
sys.path.append("/".join(os.path.dirname(__file__).split("/")[:-3]))

from importing_modules.differents_folders.modules import callee
callee.say_hello2()
# print(os.path.dirname(__file__))
# print()
# print("/".join(os.path.dirname(__file__).split("/")[:-3]))
# n=2
# if n > 0:
#     import callee
#     callee.say_hello()