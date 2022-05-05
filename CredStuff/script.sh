#!/bin/sh
awk '{if(NR==378) print $0}' passwords.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m' > flag.txt