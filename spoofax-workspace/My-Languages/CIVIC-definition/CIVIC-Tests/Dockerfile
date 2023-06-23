# Dockerfile

FROM gcc:latest

# Make sure that all system packages are latest versions
RUN apt-get update && apt-get upgrade -y

# Install software-properties-common (for add-apt-repository)
RUN apt-get install -y software-properties-common

# Add ubuntu-toolchain-r/test
#RUN add-apt-repository ppa:ubuntu-toolchain-r/test
#
# Install the latest g++
#RUN apt-get update && apt-get install -y g++
#
# Set the working directory
WORKDIR /usr/src

