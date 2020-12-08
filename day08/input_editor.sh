#!/bin/bash

for i in $(grep  'nop' loop.txt |cut -f 1 -d' '); do cp input_ input.n${i};  sed -i "${i}s/nop/jmp/" input.n${i}; done
for i in $(grep  'jmp' loop.txt |cut -f 1 -d' '); do cp input_ input.j${i};  sed -i "${i}s/jmp/nop/" input.j${i}; done

for inputfile in `ls input.n* input.j*`
do
	echo $inputfile
	cp $inputfile input
	python3 task2.py
done
