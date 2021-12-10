"""
This script is used to generate a bunch of positive
regression tests using the .tiff images in valid_tiffs
for cve_2016_10092-multi-pos
"""

#${{TEST_EXECUTION_PREFIX:-}} "${{PATH_BIN}}" -i "${{PATH_TEST_TIFF}}" foo

text_case_template_text = """
#!/bin/bash
set -eu

HERE_DIR=$( cd "$( dirname "${{BASH_SOURCE[0]}}" )" && pwd )
BASE_TIFF_PATH="${{HERE_DIR}}/valid_tiffs/"
PATH_BIN="${{1:-${{HERE_DIR}}/source/dbuild/tools/{toolName}}}"

${{TEST_EXECUTION_PREFIX:-}} "${{PATH_BIN}}" {testExecution}
x=$?

if [[ -e "${{HERE_DIR}}/BUG.cfg" ]]; then 
PATH_BIN="${{1:-${{HERE_DIR}}/source/fbuild/tools/{toolName}}}"
if [[ -e $PATH_BIN ]]; then 
${{TEST_EXECUTION_PREFIX:-}} "${{PATH_BIN}}" {testExecution}
x=$?
fi
fi

exit $x

"""
from os import listdir
from os.path import isfile, join
import os
import stat

def get_valid_tiff_names(tiffs_folder_loc):
    """
    Gets the name of all tiff files in sorted order
    """
    return sorted([tf for tf in listdir(tiffs_folder_loc) if isfile(join(tiffs_folder_loc, tf))])
    

def make_test_case(test_num, tiff1, tiff2, tiff3, toolName, testExecution):
    """
    Makes the file with the specified test case
    """
    with open('test-' + str(test_num), 'w') as test_file:
        test_file.write(text_case_template_text.format(tiff1=tiff1, tiff2=tiff2, tiff3=tiff3, 
                                                        toolName=toolName, 
                                                        testExecution=testExecution))
        st = os.stat('test-' + str(test_num))
        os.chmod('test-' + str(test_num), st.st_mode | stat.S_IEXEC)

# #${{TEST_EXECUTION_PREFIX:-}} "${{PATH_BIN}}" -i "${{PATH_TEST_TIFF}}" foo
def generate_tiffcrop_execution_line(tiff1, tiff2, tiff3):
    el = []
    el.append('tiffcrop -c lzw "${{BASE_TIFF_PATH}}{0}" "${{BASE_TIFF_PATH}}{1}" result.tiff'.format(tiff1, tiff2))
    el.append('tiffcrop -c lzw "${{BASE_TIFF_PATH}}{0}" "${{BASE_TIFF_PATH}}{1}" result.tiff'.format(tiff1, tiff3))
    el.append('tiffcrop -c lzw "${{BASE_TIFF_PATH}}{0}" "${{BASE_TIFF_PATH}}{1}" result.tiff'.format(tiff2, tiff3))
    el.append('tiffcrop -F horiz "${{BASE_TIFF_PATH}}{0}"'.format(tiff1))
    el.append('tiffcrop -F vert "${{BASE_TIFF_PATH}}{0}"'.format(tiff2))
    el.append('tiffcrop -i lzw "${{BASE_TIFF_PATH}}{0}" "${{BASE_TIFF_PATH}}{1}"'.format(tiff1, tiff2))
    el.append('tiffcrop -i lzw "${{BASE_TIFF_PATH}}{0}" "${{BASE_TIFF_PATH}}{1}"'.format(tiff1, tiff3))
    el.append('tiffcrop -i lzw "${{BASE_TIFF_PATH}}{0}" "${{BASE_TIFF_PATH}}{1}"'.format(tiff2, tiff3))
    return(el)


def generate_execution_line(tiff1, tiff2, tiff3, toolName):
    """
    This function generates the appropriate execution line for the given 'toolname'
    toolname: a binary in libtiff/tools
    returns a list of possible execution lines with the givin tiffs and tools
    """
    if toolName == 'tiffcrop':
        return generate_tiffcrop_execution_line(tiff1, tiff2, tiff3)

def make_tests(toolName, num_tests):
    valid_tiffs = get_valid_tiff_names('valid_tiffs')
    test_num = 2
    for i in range(0, len(valid_tiffs) - 3, 3):
        tiff1, tiff2, tiff3 = valid_tiffs[i], valid_tiffs[i + 1], valid_tiffs[i + 2]
        executionLines = generate_execution_line(tiff1, tiff2, tiff3, toolName)
        for el in executionLines:
            make_test_case(test_num, tiff1, tiff2, tiff3, toolName, el)
            test_num += 1
            num_tests -= 1
            if num_tests == 0:
                return


if __name__ == "__main__":
    make_tests('tiffcrop', 10)
