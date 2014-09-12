#!/bin/bash

echo "Current input"

cat mp2.in

echo ""
echo "Replace cc-pvdz by 6-31G*"
echo "  and change PURCAR 111 to PURCAR 222"
echo ""

cat mp2.in | sed 's/cc-pvdz/6-31G\*/g' | sed 's/111/222/g'

# This also work:
# sed 's/cc-pvdz/6-31G\*/g' -f mp2.in

# To actually overwrite changes in current file:
# sed 's/cc-pvdz/6-31G\*/g' -fi mp2.in


