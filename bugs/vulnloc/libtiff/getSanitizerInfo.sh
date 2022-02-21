#!/bin/bash

#Make a folder at the benchmark level to

STORAGE_FOLDER="/benchmarks/SanitizerResults"
mkdir -p $STORAGE_FOLDER
CURRENT_BUG="$(basename "`pwd`")"
#cleans the slate
./clean

# Builds using the address sanitizer
#CC=clang REPAIR_TOOL=none CFLAGS="-fsanitize=address -g -fno-omit-frame-pointer" CXXFLAGS="-fsanitize=address" ./prebuild
#CC=clang REPAIR_TOOL=none CFLAGS="-fsanitize=address -g -fno-omit-frame-pointer" CXXFLAGS="-fsanitize=address" ./build
#ASAN_OPTIONS=symbolize=0 ./test 2> "${STORAGE_FOLDER}/addressSan.txt"

#builds using the memory sanitizer
#./clean
#CC=clang REPAIR_TOOL=none CFLAGS="-fsanitize=undefined -g -fno-omit-frame-pointer" CXXFLAGS="-fsanitize=undefined" ./prebuild
#CC=clang REPAIR_TOOL=none CFLAGS="-fsanitize=undefined -g -fno-omit-frame-pointer" CXXFLAGS="-fsanitize=undefined" ./build
#ASAN_OPTIONS=symbolize=0 ./test 2> "${STORAGE_FOLDER}/undefinedSan.txt"

# Builds using both 
./clean
CC=clang-11 REPAIR_TOOL=none CFLAGS="-fsanitize=undefined,address -g -fno-omit-frame-pointer" CXXFLAGS="-fsanitize=undefined,address" ./prebuild
CC=clang-11 REPAIR_TOOL=none CFLAGS="-fsanitize=undefined,address -g -fno-omit-frame-pointer" CXXFLAGS="-fsanitize=undefined,address" bear ./build
UBSAN_OPTIONS=print_stacktrace=1 ASAN_OPTIONS=symbolize=0 ./test 2> "${STORAGE_FOLDER}/bothSan.txt"

exit 0
