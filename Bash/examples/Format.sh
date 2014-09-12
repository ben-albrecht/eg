#!/bin/sh

#	Format.sh	version 1
#	This script creates inputs (.in) and batch files (.pbs) based on the Gaussian inputs 
#	provided by MSD (.g03)
#	There is also a comments section created for the purpose of identification (solvent)


#Gaq = aqueous solutions (solvent = water)       	 
cd Gaq

#file= .g03 file (The Gaussian input file)
for file in *.g03 ; do	
 
   ### standard .in input file ###   
   ###                         ###

   #input= .in file ; obtains input file ; creates input files using format.awk
   input=`ls $file|sed ' s/g03/in/ ' `
   ../format.awk $file > $input		
   
   \echo "$input"    

   ### additional options ###
   ###                    ###

   #BASISline= line in which BASIS is on, official reference point inside $rem
   BASISline=`grep -n BASIS $input | awk 'BEGIN{FS=":"}{print $1}'` 
  
   #solvent= SOLVENT: * in .g03, obtained for SMX_SOLVENT
   solvent=`grep -i "SOLVENT:" $file | awk '{print $2}' `
   \echo "SOLVENT: $solvent"
 
   #directory= DIRECTORY: * in .g03, obtained for general use
   directory=`grep -i "DIRECTORY:" $file | awk '{print $2}' `
   \echo "DIRECTORY: $directory"

   #Inserting SMX_SOLVENT $solvent below BASIS in $rem section
  # awk -v "n=$BASISline" -v "s=$solvent" '(NR==n) {print "SMX_SOLVENT", s } 1' $input > .$input.temp	
  # cat .$input.temp > $input						
  # rm -f $input.temp
  
  # \echo "BASISLINE: $BASISline"
  # \echo $file
   

   ### .pbs batch file ###
   ###                 ###
   #molecule= $solvent$molecule without any ending
   molecule=`ls $file| sed 's/.g03// ' `
   cat ../template.pbs|sed s/molecule/$molecule/g > $molecule.pbs

   \echo "$molecule"

   ### comments section ###

   echo "\$comment" > c_temp.txt
   echo "SOLVENT: $solvent" >> c_temp.txt
   echo "DIRECTORY: $directory" >> c_temp.txt 
   echo "\$end" >> c_temp.txt
   cat c_temp.txt >> $input
   rm -f c_temp.txt

done

cd ../

cd Gnonaq

for file in *.g03 ; do	
 
   ### standard .in input file ###   
   ###                         ###

   #input= .in file ; obtains input file ; creates input files using format.awk
   input=`ls $file|sed ' s/g03/in/ ' `
   ../format.awk $file > $input		
   
   \echo "$input"    

   ### additional options ###
   ###                    ###

   #BASISline= line in which BASIS is on, official reference point inside $rem
   BASISline=`grep -n BASIS $input | awk 'BEGIN{FS=":"}{print $1}'` 
  
   #solvent= SOLVENT: * in .g03, obtained for SMX_SOLVENT
   solvent=`grep -i "SOLVENT:" $file | awk '{print $2}' `
   \echo "SOLVENT: $solvent"
 
   #directory= DIRECTORY: * in .g03, obtained for general use
   directory=`grep -i "DIRECTORY:" $file | awk '{print $2}' `
   \echo "DIRECTORY: $directory"

   #Inserting SMX_SOLVENT $solvent below BASIS in $rem section
  # awk -v "n=$BASISline" -v "s=$solvent" '(NR==n) {print "SMX_SOLVENT", s } 1' $input > .$input.temp	
  # cat .$input.temp > $input						
  # rm -f $input.temp
  
#   \echo "BASISLINE: $BASISline"
 #  \echo $file
   

   ### .pbs batch file ###
   ###                 ###
   #molecule= $solvent$molecule without any ending
   molecule=`ls $file| sed 's/.g03// ' `
   cat ../template.pbs|sed s/molecule/$molecule/g > $molecule.pbs

   \echo "$molecule"


   ### comments section ###

   echo "\$comment" > c_temp.txt
   echo "SOLVENT: $solvent" >> c_temp.txt
   echo "DIRECTORY: $directory" >> c_temp.txt
   echo "\$end" >> c_temp.txt
   cat c_temp.txt >> $input
   rm -f c_temp.txt

done
cd ../

