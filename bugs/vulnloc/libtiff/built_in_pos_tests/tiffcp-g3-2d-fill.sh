#!/bin/sh
#
# Basic sanity check for tiffcp with G3 compression, 2 dimensional
# encoding, and zero-filled boundaries.
#
. /workspace/built_in_pos_tests/common.sh
f_test_convert "${TIFFCP} -c g3:2d:fill" "${IMG_MINISWHITE_1C_1B}" "o-tiffcp-g3-2d-fill.tiff"
