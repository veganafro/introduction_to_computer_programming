#!/bin/sh

echo "### Testing grade.py\n"
grade_out="$((python3 grade.py <<EOF
-12
EOF
) 2>&1)
$((python3 grade.py <<EOF
69
EOF
) 2>&1)"

if [[ "${grade_out}" == *"translate"* ]] && \
    [[ "${grade_out}" == *"D"* ]]; then
        echo "VVV All grade.py tests pass\n"
    else
        echo "XXX Some grade.py tests do not pass\n"
    fi

echo "${grade_out}\n"


echo "### Testing tip.py\n"
tip_out="$((python3 tip.py <<EOF
6
10
EOF
) 2>&1)
$((python3 tip.py <<EOF
3
20
good
EOF
) 2>&1)"

if [[ "${tip_out}" == *'$2'* ]] && \
    [[ "${tip_out}" == *'$4'* ]]; then
        echo "VVV All"
