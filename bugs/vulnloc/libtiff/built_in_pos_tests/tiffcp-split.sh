#!/bin/sh
#
# Basic sanity check for tiffcp + tiffsplit
#
# First we use tiffcp to join our test files into a multi-frame TIFF
# and then we use tiffsplit to split them out again.
#
. /workspace/built_in_pos_tests/common.sh
conjoined=o-tiffcp-split-conjoined.tif
splitfile=o-tiffcp-split-split-

f_test_convert "${TIFFCP}" "${IMG_UNCOMPRESSED}" "${conjoined}"
f_test_convert "${TIFFSPLIT}" "${conjoined}" "${splitfile}"