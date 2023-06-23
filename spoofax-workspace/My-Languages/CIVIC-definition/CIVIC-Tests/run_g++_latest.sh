#!/bin/bash

# Function to start the container
start_container() {
    # Start a container with the official GCC image, name it 'cpp_container', mount the current directory into the container's working directory
    sudo docker run --name cpp_container -v $(pwd):/usr/src/myapp -td gcc:latest
}

# Function to pass the file to the container and run the file in the container with g++
run_cpp_in_container() {
    # Copy the file into the container, compile and run it
    sudo docker exec -it cpp_container /bin/bash -c "g++ -O0 -std=c++2b -o output /usr/src/myapp/$1 && ./output"
}

# Function to stop and remove the container
stop_container() {
    sudo docker stop cpp_container
    sudo docker rm cpp_container
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

start_container
run_cpp_in_container $1
stop_container
