#!/bin/sh
echo "### Testing multiply.py\n"
multiply_out=$((python3 multiply.py <<EOF
17
EOF
) 2>&1)

if [ "${multiply_out}"=~34 ] && \
    [ "${multiply_out}"=~51 ] && \
    [ "${multiply_out}"=~85 ] && \
    [ "${multiply_out}"=~119 ] && \
    [ "${multiply_out}"=~187 ] && \
    [ "${multiply_out}"=~221 ] && \
    [ "${multiply_out}"=~289 ]; then
    echo "VVV All multiply.py tests pass\n"
    echo "${multiply_out}\n"
else
    echo "XXX Some multiply.py tests do not pass\n"
    echo "${multiply_out}\n"
fi

echo "### Testing grade_bot_3000.py"
grade_bot_out=$((python3 grade_bot_3000.py <<EOF
Derp
50
68
69
70
68
70
EOF
) 2>&1)

echo "### Testing change_puhleeese.py"
change_out=$((python3 change_puhleeese.py <<EOF
Bobble derp
10
6
Derp bobble
10
9
Dobble
10
69
999
EOF
) 2>&1)
