#!/bin/sh
. /workspace/built_in_pos_tests/common.sh
infile="$IMG_MINISBLACK_1C_8B_PGM"
outfile="o-ppm2tiff_pgm.tiff"
f_test_convert "$PPM2TIFF" $infile $outfile
f_tiffinfo_validate $outfile
