#!/bin/bash

mkdir -p dependencies

git clone https://github.com/plancomps/CBS-beta dependencies/CBS-beta
git clone https://github.com/plancomps/funcons-tools dependencies/funcons-tools
git clone https://github.com/plancomps/funcons-intgen dependencies/funcons-intgen

cd dependencies/funcons-tools
cabal build
cabal install
cd -
cd dependencies/funcons-intgen
cabal build
cabal install
cd -
