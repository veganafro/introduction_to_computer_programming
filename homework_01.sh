#!/bin/sh
echo "### Testing mad_libs_lyrics.py\n"
python3 mad_libs_lyrics.py
echo ""

echo "### Testing exercises.py\n"
python3 exercises.py
echo ""

echo "### Testing tree.py\n"
python3 tree.py
echo ""

echo "### Testing numbers.py\n"
echo "Input test value: "
read test_val
echo "\n"
python3 numbers.py <<EOF
$test_val
EOF
echo ""
