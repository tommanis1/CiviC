#!/bin/bash

if [ $# -lt 1 ]; then
  echo "Usage: $0 <command> [arguments]"
  exit 1
fi

command="$@"
ulimit -Sv 6000000 && eval "$command"

