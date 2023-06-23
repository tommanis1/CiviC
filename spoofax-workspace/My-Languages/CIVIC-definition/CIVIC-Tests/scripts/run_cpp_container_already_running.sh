#!/bin/bash

# Function to pass the file to the container and compile the file in the container with g++
compile_cpp_in_container() {
    # Copy the file into the container and compile it
    sudo docker exec -it cpp_container /bin/bash -c "g++ -std=c++2b -o output /usr/src/myapp/$1"
}

# Usage of the script
if [ $# -ne 1 ]; then
    echo "Usage: $0 <cpp file>"
    exit 1
fi

# Check if the file exists
if [ ! -f $1 ]; then
    echo "Error: $1 does not exist."
    exit 1
fi

compile_cpp_in_container $1
