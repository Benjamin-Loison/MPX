#!/bin/sh

max=0
maxSpecies=""

for d in speciesNiceSpelled/*/ ; do
    #echo "$d"
	v=$(ls "$d" | wc -l)
	if [ $v -gt $max ];
	then
		max=$v;
		species="$d";
	fi;

done

echo $species
echo $max
