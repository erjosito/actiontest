#!/usr/bin/bash

# Sample file to create a version of an existing file
# Dumps the base64-encoded version of a file provided
#   as parameter in a new file

cat "$1" | base64 > "$1.base64"