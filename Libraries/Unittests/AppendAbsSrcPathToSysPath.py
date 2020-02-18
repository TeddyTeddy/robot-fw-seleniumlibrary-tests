import sys
import os
import re


def grab_modules_under_test():
    current_abs_path = os.path.abspath(os.getcwd())     # gets the current abs path to this py file
    m = re.match('(.+)\/Unittests', current_abs_path)   # grabs everything from current_abs_path except '/UnitTests' string
    src_abs_path = m.groups()[0] + '/Src'               # forms src_abs_path from the grabbed string
    sys.path.append(src_abs_path)                       # sets src_abs_path to path