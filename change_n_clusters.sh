#!/bin/bash

# Get a list of all files ending with '_settings.yml'
files=$(find . -maxdepth 1 -type f -name '*_settings.yml')

# Loop through each file
for file in $files; do

    # Replace all instances of 'q: 5' with 'q: 3'
    sed -i 's/q: 3/q: 5/g' "$file"

    # Replace all instances of 'n_clusters: 2' with 'n_clusters: 1'
    sed -i 's/n_clusters: 1/n_clusters: 2/g' "$file"

done

