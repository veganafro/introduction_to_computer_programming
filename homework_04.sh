echo "### Testing many_words.py\n"

many_words_out=$((
		    python3 many_words.py <<EOF
		    4
		    program
		    my
		    out
		    check
		    EOF
		) 2>&1)

if [[ $many_words_out == *"check out my program"*]]; then
    echo "VVV All many_words.py tests pass\n"
else
    echo "XXX Some many_words.py tests do not pass\n"


echo "### Done testing many_workds.py\n"


echo "### Testing odd_and_evens.py"



echo "### Done testing odd_and_evens.py"


echo "### Testing flagged.py"



echo "### Done testing flagged.py"


echo "### Testing average_word.py"



echo "### Done testing average_word.py"


echo "### Testing counting.py"



echo "### Done testing counting.py"
