#!/bin/sh

echo "### Testing slashes.py\n"

slashes_out=$(
    (
	python3 slashes.py <<-EOF
	
	EOF
    ))
