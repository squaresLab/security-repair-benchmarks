#!/bin/sh
#
# Basic sanity check for tiffcp with LZW Old-LZW decompression
#
. /workspace/built_in_pos_tests/common.sh
f_test_convert "${TIFFCP} -c none" "${IMG_QUAD_LZW_COMPAT}" "o-tiffcp-lzw-compat.tiff"