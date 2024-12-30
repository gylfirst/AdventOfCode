#!/bin/bash

# This script is used to initialize the environment for the advent of code

# input: $1 - the year of the challenge (required, number)
# output: the script will create a folder for the year and a folder for each day of the challenge, with a template file for the story and the solution python file

# check if the year is given and is a number
if [ -z "$1" ] || ! [[ "$1" =~ ^[0-9]+$ ]]; then
    echo "Please provide a valid year for the challenge"
    exit 1
fi

# create the year folder
mkdir -p $1
cd $1

# create the day folders and the template files
for i in {1..25}; do
    mkdir -p $i
    touch $i/solution.py
    touch $i/text.md

    # add the template to the text file
    echo "# --- Day $i: ---" >> $i/text.md

    # add the template to the solution file
    echo '# Sub-Functions for the solution
def template():
    """
    Template for the solution
    """
    return 0


# Solution for part 1
def solution_1(input_value: str) -> int:
    return 0


# Solution for part 2
def solution_2(input_value: str) -> int:
    return 0' >> $i/solution.py
done

# echo the success message
echo "The environment for the advent of code $1 has been initialized successfully!"
