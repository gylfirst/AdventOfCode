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
done

# echo the success message
echo "The environment for the advent of code $1 has been initialized successfully!"
