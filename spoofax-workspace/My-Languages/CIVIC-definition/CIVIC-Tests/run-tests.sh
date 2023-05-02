#!/bin/bash

# runfct="funcons-unstable"
runfct=$(whereis -b runfct | cut -d' ' -f2)
fileext="civ"
lang="CIVIC"

function run-test {
  testTitle=$1
  testName=$2
  testDir=$3
  echo "Test ${testTitle}:"
  echo "===== Program =====" > ${testDir}/${testName}.output
  cat ${testDir}/${testName}.$fileext >> ${testDir}/${testName}.output
  echo "===================" >> ${testDir}/${testName}.output
  ${runfct} --non-deterministic value-operations,rules,pattern-matching,interleaving-of-args ${testDir}/${testName}.fct >> ${testDir}/${testName}.output
}

echo -e "\nRunning Tests"

for dir in */; do
  if [[ -d "$dir" && -n "$(ls -A "$dir"/*.fct 2>/dev/null)" ]]; then
    echo "Directory: $dir"
    for fct_file in $dir/*.fct; do
      testName=$(basename "$fct_file" .fct)
      run-test "$testName" "$testName" "$dir"
    done
    echo ""
  fi
done
