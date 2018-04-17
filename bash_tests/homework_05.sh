#!/bin/sh

echo "### Testing slashes.py\n"

slashes_out=$(
    (
		python3 slashes.py <<-EOF
		3
		2
		EOF
    ) 2>&1)

if [[ "${slashes_out}" == *"|/|
|\\|"* ]]; then
    echo "VVV All slashes.py tests pass\n"
else
    echo "XXX Some slashes.py tests do not pass\n"
fi

echo "${slashes_out}\n###Done testing slashes.py\n"

echo "### Running unit tests\n"

cp ~/github/grading_tests/unit_tests/homework_05.py .
python3 homework_05.py

echo "### Done running unit tests\n"

echo "### Testing feeling_quizzy.py\n"

quizzy_out=$(
	(
		python3 feeling_quizzy.py <<-EOF
		2
		3
		dddd
		X
		3
		6
		9
		69
		EOF
	) 2>&1)

echo "${quizzy_out}\n###Done testing feeling_quizzy.py\n"
