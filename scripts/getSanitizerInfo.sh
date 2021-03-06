#!/bin/bash

#Make a folder at the benchmark level to

STORAGE_FOLDER="/benchmarks/SanitizerResults"
mkdir $STORAGE_FOLDER
CURRENT_BUG="$(basename "`pwd`")"
#cleans the slate
./clean

# Builds using the address sanitizer
CC=clang REPAIR_TOOL=none CFLAGS="-fsanitize=address -g -fno-omit-frame-pointer" CXXFLAGS="-fsanitize=address" ./prebuild
CC=clang REPAIR_TOOL=none CFLAGS="-fsanitize=address -g -fno-omit-frame-pointer" CXXFLAGS="-fsanitize=address" ./build
./test 2> "${STORAGE_FOLDER}/${CURRENT_BUG}_addressSan.txt"

#builds using the memory sanitizer
./clean
CC=clang REPAIR_TOOL=none CFLAGS="-fsanitize=undefined -g -fno-omit-frame-pointer" CXXFLAGS="-fsanitize=undefined" ./prebuild
CC=clang REPAIR_TOOL=none CFLAGS="-fsanitize=undefined -g -fno-omit-frame-pointer" CXXFLAGS="-fsanitize=undefined" ./build
./test 2> "${STORAGE_FOLDER}/${CURRENT_BUG}_undefinedSan.txt"

# Builds using both 
./clean
CC=clang REPAIR_TOOL=none CFLAGS="-fsanitize=undefined,address -g -fno-omit-frame-pointer" CXXFLAGS="-fsanitize=undefined,address" ./prebuild
CC=clang REPAIR_TOOL=none CFLAGS="-fsanitize=undefined,address -g -fno-omit-frame-pointer" CXXFLAGS="-fsanitize=undefined,address" ./build
./test 2> "${STORAGE_FOLDER}/${CURRENT_BUG}_bothSan.txt"
