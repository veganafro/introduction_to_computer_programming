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
else
    echo "XXX Some multiply.py tests do not pass\n"
fi

echo "${multiply_out}\n"

echo "### Testing grade_bot_3000.py\n"
grade_bot_out=$((python3 grade_bot_3000.py <<EOF
Derp
Intro to Derping
70
89
73
30
95
99
EOF
) 2>&1)

if [ "${grade_bot_out}"=~81.00 ] && \
    [ "${grade_bot_out}"=~97.00 ] && \
    [ "${grade_bot_out}"=~85.80 ]; then
        echo "VVV All grade_bot_3000.py tests pass\n"
else
    echo "XXX Some grade_bot_3000.py tests do not pass\n"
fi

echo "${grade_bot_out}\n"

echo "### Testing change_puhleeese.py\n"
change_out=$((python3 change_puhleeese.py <<EOF
Bobble derp
10
3
Derp bobble
10
9
Dobble
10
69
999
EOF
) 2>&1)

if [ "${change_out}"=~30.00  ] && \
    [ "${change_out}"=~29.99 ] && \
    [ "${change_out}"=~37.50 ] && \
    [ "${change_out}"=~97.49 ] && \
    [ "${change_out}"=~8.65 ] && \
    [ "${change_out}"=~106.14 ] && \
    [ "${change_out}"=~150.03 ] && \
    [ "${change_out}"=~43.89 ]; then
        echo "VVV All change_puhleeese.py tests pass\n"
else
    echo "XXX Some change_puhleeese.py tests do not pass\n"
fi

echo "${change_out}"
