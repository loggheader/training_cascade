#!/bin/bash
if [ $# -ne 2 ]; then
	printf "Error. Expected format is:\n./cut_positives.sh [ subfolder inside positives folder] [ name of accept info]\n"
else
	echo Writing to data/accept_info/$2 from data/positives/$1
	printf "\ny/n?\n"
	read   answer
	if [ $answer == "y" ]; then
		opencv_annotation --images=data/positives/$1/ --annotations=data/accept_info/$2
	fi
fi


