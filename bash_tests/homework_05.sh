#!/bin/sh

echo "### Testing slashes.py\n"

slashes_out=$(
    (
	python3 slashes.py <<-EOF
	3
	2
	EOF
    ) 2>&1)

if [[ "${slashes_out}" == *"|/|\n|\\|\n|/|"* ]]; then
    echo "VVV All slashes.py tests pass\n"
else
    echo "XXX Some slashes.py tests do not pass\n"
fi

echo "${slashes_out}\n###Done testing slashes.py\n"
