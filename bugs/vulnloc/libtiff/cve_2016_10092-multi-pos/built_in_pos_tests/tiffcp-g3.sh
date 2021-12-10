#!/bin/sh
#
# Basic sanity check for tiffcp with G3 compression
#
. /workspace/built_in_pos_tests/common.sh
f_test_convert "${TIFFCP} -c g3" "${IMG_MINISWHITE_1C_1B}" "o-tiffcp-g3.tiff"