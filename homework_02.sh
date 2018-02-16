#!/bin/sh
echo "### Testing multiply.py"
multiply_out = $((python3 multiply.py <<EOF
2
EOF
) 2>&1)

echo "### Testing grade_bot_3000.py"
grade_bot_out = $((python3 grade_bot_3000.py <<EOF
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
change_out = $((python3 change_puhleeese.py <<EOF
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
