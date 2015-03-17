#!/bin/sh

for file in */hfx*.out; do
    echo $file
    grep "HOMO - LUMO gap" $file | awk '{print $7}' >> homolumo.dat

done
