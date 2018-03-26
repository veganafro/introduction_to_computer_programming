#!/bin/sh

echo "### Testing many_words.py\n"

many_words_out=$(
    (
	python3 many_words.py <<-EOF
	4
	program
	my
	out
	check
	EOF
    ) 2>&1)

if [[ "${many_words_out}" == *"check out my program"* ]]; then
    echo "VVV All many_words.py tests pass\n"
else
    echo "XXX Some many_words.py tests do not pass\n"
fi

echo "${many_words_out}\n### Done testing many_workds.py\n"


echo "### Testing odds_and_evens.py\n"

odds_and_evens_out_1=$(
    (
	python3 odds_and_evens.py <<-EOF
	Derp
	odds
	0
	EOF
    ) 2>&1)

odds_and_evens_out_2=$(
    (
	python odds_and_evens.py <<-EOF
	evens
	2
	1
	1
	EOF
    ) 2>&1)

if [[ "${odds_and_evens_out_1}" == *"NO ONE"* ]] && \
       [[ "${odds_and_evens_out_2}" == *"wins"* ]]; then
    echo "VVV All odds_and_evens.py tests pass\n"
else
    echo "XXX Some odds_and_evens.py tests do not pass\n"
fi

echo "${odds_and_evens_out_1}\n${odds_and_evens_out_2}\n### Done testing odd_and_evens.py\n"


echo "### Testing flagged.py\n"

flagged_out=$(
    (
	python3 flagged.py <<-EOF
	0
	5
	$
	EOF
    ) 2>&1)

if [[ "${flagged_out}" == *"$$$$$
 $$$$
  $$$
   $$
    $
   $$
  $$$
 $$$$
$$$$$"* ]]; then
    echo "VVV All flagged.py tests pass\n"
else
    echo "XXX Some flagged.py tests do not pass\n"
fi

echo "${flagged_out}\n### Done testing flagged.py\n"


echo "### Testing counting.py\n"

counting_out=$(
    (
	python3 counting.py
    ) 2>&1)

if [[ "${counting_out}" == *"while loops
2
4
6
8
10
5
4
3
2
1
for loops
2
4
6
8
10
5
4
3
2
1"* ]]; then
    echo "VVV All counting.py tests pass\n"
else
    echo "XXX Some counting.py tests do not pass\n"
fi

echo "${counting_out}\n### Done testing counting.py\n"
