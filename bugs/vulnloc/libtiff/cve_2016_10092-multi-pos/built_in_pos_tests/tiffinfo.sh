#!/bin/sh
#
# Basic sanity check for tiffinfo.
#
. /workspace/built_in_pos_tests/common.sh
f_test_reader "${TIFFINFO} -c -D -d -j -s " "${IMG_MINISBLACK_1C_16B}"
