#!/usr/bin/env bash

if [ $# != 1 ]
  then
    echo "One argument must be supplied - dataset folder name. Be careful, this must be snake_case_name."
fi

cd datasets

mkdir $1
mkdir $1/data

cp template_readme.md $1/README.md
cp template.ipynb $1/$1.ipynb

echo "Folder structure for $1 sucessfully created in datasets/ directory. Do not forget to add data to data/ directory and change README.md and $1.ipynb files."
