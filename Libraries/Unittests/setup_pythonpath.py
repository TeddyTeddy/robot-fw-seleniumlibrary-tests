import os
import re


if __name__ == '__main__':
    current_abs_path = os.path.abspath(os.getcwd())     # gets the current abs path to this py file
    sep = os.path.sep  # get os specific path seperator (either '\' for Windows or '/' for linux)
    pattern = f'(.+){sep}Unittests'
    # grabs everything from current_abs_path except '/UnitTests' string
    m = re.match(pattern, current_abs_path)
    src_abs_path = f'{m.groups()[0]}{sep}Src{sep}'               # forms src_abs_path from the grabbed string
    unittests_common_abs_path = f'{current_abs_path}{sep}Common{sep}'
    result = src_abs_path + os.path.pathsep + unittests_common_abs_path
    if 'PYTHONPATH' in os.environ:
        if result in os.environ['PYTHONPATH']:
            # if result already is included in PYTHONPATH, use PYTHONPATH as it is
            result = os.environ['PYTHONPATH']
        else:
            # if result is not included in PYTHONPATH, then result will extend PYTHONPATH
            result = os.environ['PYTHONPATH'] + os.path.pathsep + result
    else:
        pass
    file = open('pythonpath.txt', 'w+')  # re-formats file contents, under the same folder as run command
    file.write(result)
    file.close()


