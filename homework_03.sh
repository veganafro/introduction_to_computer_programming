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
        echo "VVV All tip.py tests pass\n"
    else
        echo "XXX Some tip.py tests do not pass\n"
    fi

echo "${tip_out}\n"


echo "### Testing adventure.py\n"
adventure_out="$((python3 adventure.py <<EOF
Derp
Programmer
EOF
) 2>&1)
$((python3 adventure.py <<EOF
Derp
Wizard
open
EOF
) 2>&1)
$((python3 adventure.py <<EOF
Derp
Warrior
leave
EOF
) 2>&1)"

echo "${adventure_out}\n"

echo "### Testing triangle_or_not.py\n"
triangle_out="$((python3 triangle_or_not.py <<EOF
1
1
2
2
2
1
EOF
) 2>&1)
$((python3 triangle_or_not.py <<EOF
1
1
2
2
3
3
EOF
) 2>&1)"

if [[ "${triangle_out}" == *"HAZ"* ]] && \
    [[ "${triangle_out}" == *"Nope"* ]]; then
        echo "VVV All triangle_or_not.py tests pass\n"
    else
        echo "XXX Some triangle_or_not.py tests do not pass\n"
    fi

echo "${triangle_out}\n"
