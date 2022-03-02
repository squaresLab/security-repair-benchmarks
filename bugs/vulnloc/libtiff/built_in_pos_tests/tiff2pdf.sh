#!/bin/sh
#
# Basic sanity check for tiff2pdf
#
. /workspace/built_in_pos_tests/common.sh
f_test_stdout "${TIFF2PDF}" "${IMG_MINISWHITE_1C_1B}" "o-tiff2pdf.pdf"