#! /bin/bash

#Exit when error
set -o errexit
#Check for any unset variables
set -o nounset

#Defining a function called main
main()
{
	input=$1	#Take the first argument
	len=${#input}	#Take the length of the argument
	reverse=""	#Initialize an empty string
	
	#Run a for loop to get reverse of the string
	for((i=$len-1;i>=0;i--()
	do 
		reverse=$reverse${input:$i:1}
	done
	#Output reversed string
	echo "$reverse"
}

#Calling the main function with all the arguments to avoid white space errors
main "$@"
