import os
import re


if __name__ == '__main__':
    current_abs_path = os.path.abspath(os.getcwd())     # gets the current abs path to this py file
    sep = os.path.sep  # get os specific path seperator (either '\' for Windows or '/' for linux)
    pattern = f'(.+)\{sep}Unittests'
    # grabs everything from current_abs_path except '/UnitTests' string
    m = re.match(pattern, current_abs_path)
    src_abs_path = f'{m.groups()[0]}{sep}Src{sep}'               # forms src_abs_path from the grabbed string
    unittests_common_abs_path = f'{current_abs_path}{sep}Common{sep}'
    paths = [src_abs_path, unittests_common_abs_path]
    result = ''
    if 'PYTHONPATH' in os.environ:
        is_path_added = False
        for p in paths:
            if p in os.environ['PYTHONPATH']:
                # if p already is included in PYTHONPATH, do nothing
                pass
            else:
                # if p is not included in PYTHONPATH, then result will contain p
                if result:
                    result = f'{os.path.pathsep}'.join([p,result])
                else:
                    result = p
                is_path_added = True

        if is_path_added:
            result = os.environ['PYTHONPATH'] + os.path.pathsep + result
    else:
        result = f'{os.path.pathsep}'.join(paths)
    file = open('pythonpath.txt', 'w+')  # re-formats file contents, under the same folder as run command
    file.write(result)
    file.close()
