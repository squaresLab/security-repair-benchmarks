#!/bin/bash

# Set up docker environment to get the line numbers

#Go through each bug needed and do the steps below:
cp /benchmarks/getSanitizerInfo.sh .
for program in "libtiff" "coreutils" "libxml2" "binutils"
do
    echo $program
    
    # Move into the program directory
    cd $program

    for bug in ./*
    do
        # If it's not a directory, keep going
        [ -d "{path}" ] || continue
        thisBugFolder="(basename "${path}")"

        #FIXME: have another check for if it's a "bad" directory
        
        cd $thisBugFolder
        cp /benchmarks/getSanitizerInfo.sh .
        chmod u+x getSanitizerInfo.sh 
        ./getSanitizerInfo.sh 
        cd ..

    done

    # Move back to original directory
    cd ..
done