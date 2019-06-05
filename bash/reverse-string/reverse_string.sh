#! /bin/bash

set -o errexit
set -o nounset

main()
{
	input=$1
	len=${#input}
	reverse=""
	for((i = $len - 1; i >= 0; i--))
	do 
		reverse=$reverse${input:$i:1}
	done
	echo "$reverse"
}

main "$@"
