#!/bin/bash

DEPENDENCIES="$(pwd)/dependencies"
cbsc=$(find "$DEPENDENCIES/funcons-intgen" -name "cbsc" -type f | sort | head -n 1)


#
#$(${cbsc} )
#


# Set the directory path
workspace_dir="spoofax-workspace"

# Search for *-definition folders and loop over them
while IFS= read -r -d '' definition_folder; do
  # Get the name by extracting the part before '-definition'
  name=$(basename "$definition_folder" | sed 's/-definition$//')

  # Find the matching *-Funcons folder and save its location
  funcons_folder=$(find "$workspace_dir" -type d -name "${name}-Funcons" -print -quit)
  funcons_file=$(find "$funcons_folder" -type f -name "${name}-Funcons.cbs" -print -quit)
  # Find the matching *-Runfct folder and save its location
  runfct_folder=$(find "$workspace_dir" -type d -name "${name}-Runfct" -print -quit)
  
  # Run cbs  
  ${cbsc} ${funcons_file} ${runfct_folder} ${name}
  # Replace the none functioning import in Main.hs
  sed -i "s/import Funcons.$name.Library/import Funcons.$name.${name}Funcons.${name}Funcons/" "$runfct_folder/Main.hs"
  # Execute cabal build in runfct_folder
  cd "$runfct_folder" || exit
  cabal build
  cabal install --overwrite-policy=always
  
  # Return to the previous directory
  cd - || exit
done < <(find "$workspace_dir" -type d -name '*-definition' -print0)
