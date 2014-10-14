#!/bin/bash

### Declaration of counters ###
i=1
j=1
q=0
i58=1
j58=1
q58=0

rm -rf MainFiles/*.txt
rm -rf MainFiles/*.in
rm -rf MainFiles/*.pbs


for Gdir in G* ; do
   cd $Gdir
   for file in *.g03 ; do
	
	directory=`grep -i "DIRECTORY:" $file | awk '{print $2}'`
	input=`ls $file|sed ' s/g03/in/ ' `
        output=`ls $file|sed ' s/g03/out/ ' `

#--------------------------G58_aq_neu----------------
	if [ $directory == "G58_aq_neu" ] ; then

          cat $input >> ../MainFiles/Q58_$j58.in
          if [ $i58 -lt 3008 ] ; then
                if [ $q58 -ne  0 -o $i58 -eq 1 ] ; then
                   echo @@@ >> ../MainFiles/Q58_$j58.in
                fi
          fi
          \echo `pwd`/$output >> ../MainFiles/ls58_pwd.txt
          \echo $i58 >> ../MainFiles/ls58_i.txt
          \echo `pwd`/$file

          i58=`expr $i58 "+" 1`
          q58=`expr $i58 "%" 5`
          \echo i58 = $i58
          \echo j58 = $j58
          \echo q58 = $q58
          
          if [ $q58 -eq 1 ] ; then
             j58=`expr $j58 "+" 1`
          fi


#--------------------------non-G58_aq_neu----------------
	else

	  cat $input >> ../MainFiles/Q_$j.in
          if [ $i -lt 3008 ] ; then
                if [ $q -ne  0 -o $i -eq 1 ] ; then
                   echo @@@ >> ../MainFiles/Q_$j.in
        	fi
          fi
          \echo `pwd`/$output >> ../MainFiles/ls_pwd.txt
          \echo $i >> ../MainFiles/ls_i.txt
          \echo `pwd`/$file

          i=`expr $i "+" 1`
          q=`expr $i "%" 100`
          \echo i = $i
          \echo j = $j
          \echo q = $q
          
	  if [ $q -eq 1 ] ; then
             j=`expr $j "+" 1`
          fi
	
	fi
                #set molecule = `ls $file|sed ' s/.g03// ' `
                #cat ../../template.pbs|sed s/molecule/$molecule/g > $molecule.pbs
    done
  cd ../
done  

# Removing extra @@@ from the final line of the final file for Q and Q58 files

cd MainFiles

echo "final j=$j"
echo "final j58=$j58"

pwd 

lineQ=`wc -l Q_$j.in| awk '{print $1}'`
lineQ58=`wc -l Q58_$j58.in| awk '{print $1}'`

awk -v "lineQ=$lineQ" 'NR == lineQ {next} {print}' Q_$j.in > .Qtemp.txt
awk -v "lineQ58=$lineQ58" 'NR == lineQ58 {next} {print}' Q58_$j58.in > .Q58temp.txt 

cat .Qtemp.txt > Q_$j.in
cat .Q58temp.txt > Q58_$j.in

rm -f .Qtemp.txt
rm -f .Q58temp.txt

# Generating batch files (.pbs)

for Qfile in Q_*.in ; do
	Qname=`ls $Qfile|sed ' s/.in//'`
	cat ../template.pbs|sed s/molecule/$Qname/g > $Qname.pbs
done

for Q58file in Q58_*.in ; do
	Q58name=`ls $Q58file|sed ' s/.in//'`
	cat ../template.pbs|sed s/molecule/$Q58name/g > $Q58name.pbs
done

#Generating Lists

paste ls_i.txt ls_pwd.txt > ls_Q.txt
paste ls58_i.txt ls58_pwd.txt > ls_Q58.txt

#Leaving Mainfiles/
cd ../
