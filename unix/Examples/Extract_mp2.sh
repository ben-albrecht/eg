#!/bin/bash

# Wrote this script in 2 minutes

echo "File: $1"

echo "SCF Energy"
grep "SCF   energy in the final basis set" mp2.out | awk '{print $9}' 

echo "MP2 Energy"
grep "MP2         total energy = " $1 | awk '{print $5}'


