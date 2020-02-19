import os
import re


if __name__ == '__main__':
    current_abs_path = os.path.abspath(os.getcwd())     # gets the current abs path to this py file
    m = re.match('(.+)\/Unittests', current_abs_path)   # grabs everything from current_abs_path except '/UnitTests' string
    src_abs_path = m.groups()[0] + '/Src/'               # forms src_abs_path from the grabbed string
    unittests_common_abs_path = current_abs_path + '/Common/'
    result = src_abs_path + ':' + unittests_common_abs_path
    if 'PYTHONPATH' in os.environ:
        if result in os.environ['PYTHONPATH']:
            # if result already is included in PYTHONPATH, use PYTHONPATH as it is
            result = os.environ['PYTHONPATH']
        else:
            # if result is not included in PYTHONPATH, then result will extend PYTHONPATH
            result = os.environ['PYTHONPATH'] + ':' + result
    else:
        pass
    file = open('needed_abs_directories.txt', 'w+')
    file.write(result)
    file.close()


