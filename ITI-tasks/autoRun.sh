#!/bin/bash

for file in *.py; do
    # Check if there are actually .py files (in case none exist)
      [[ -e "$file" ]] || continue

    echo "--- Running $file ---"
      python3 "$file"
      echo ""

done
