#!/bin/sh
# Generated file, master is Makefile.am
. /workspace/built_in_pos_tests/common.sh
infile="$srcdir/images/lzw-single-strip.tiff"
outfile="o-tiffcrop-doubleflip-lzw-single-strip.tiff"
f_test_convert "$TIFFCROP -F both" $infile $outfile
f_tiffinfo_validate $outfile