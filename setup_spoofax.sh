#!/bin/bash

# Download spoofax
wget http://artifacts.metaborg.org/service/local/repositories/releases/content/org/metaborg/org.metaborg.spoofax.eclipse.dist/2.5.16/org.metaborg.spoofax.eclipse.dist-2.5.16-linux-x64-jre.tar.gz

# Extract the contents of the tar file into the dependencies directory
tar -zxvf org.metaborg.spoofax.eclipse.dist-2.5.16-linux-x64-jre.tar.gz -C dependencies/

# Remove the original tar file
rm org.metaborg.spoofax.eclipse.dist-2.5.16-linux-x64-jre.tar.gz


# Prompt the user for the number of GB of memory to allocate
read -p "Enter the number of GB of memory to allocate to Spoofax (between 2 and 8): " mem_gb

# Check if the entered value is between 2 and 4
if (( mem_gb < 2 || mem_gb > 8 )); then
    echo "Error: You must enter a number between 2 and 8"
    exit 1
fi

# Update the -Xmx flag in eclipse.ini with the new value
sed -i "s/-Xmx[0-9]*[MG]/-Xmx${mem_gb}G/" dependencies/spoofax/eclipse.ini
echo "Spoofax memory updated to ${mem_gb}GB"


# Check if dependencies/cbs-beta-tools exists
if [ -d "dependencies/cbs-beta-tools" ]; then
  echo "Copy dependencies/cbs-beta-tools/CBS to spoofax-workspace/CBS"
  mkdir -p spoofax-workspace/CBS/
  cp -R dependencies/cbs-beta-tools/CBS/* spoofax-workspace/CBS/
else
  echo "ERROR: dependencies/cbs-beta-tools directory does not exist!"
fi


