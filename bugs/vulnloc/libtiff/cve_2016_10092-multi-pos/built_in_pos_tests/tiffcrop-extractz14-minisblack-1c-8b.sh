#!/bin/sh
# Generated file, master is Makefile.am
. /workspace/built_in_pos_tests/common.sh
infile="$srcdir/images/minisblack-1c-8b.tiff"
outfile="o-tiffcrop-extractz14-minisblack-1c-8b.tiff"
f_test_convert "$TIFFCROP -E left -Z1:4,2:4" $infile $outfile
f_tiffinfo_validate $outfile