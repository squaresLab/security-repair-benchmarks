#!/bin/sh
# Generated file, master is Makefile.am
. /workspace/built_in_pos_tests/common.sh
infile="$srcdir/images/rgb-3c-16b.tiff"
outfile="o-tiff2rgba-rgb-3c-16b.tiff"
f_test_convert "$TIFF2RGBA" $infile $outfile
f_tiffinfo_validate $outfile