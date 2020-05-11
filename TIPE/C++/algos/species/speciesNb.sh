#!/bin/sh

for d in species/speciesNiceSpelled/*/ ; do
	echo $(ls "$d" | wc -l) $d
done
