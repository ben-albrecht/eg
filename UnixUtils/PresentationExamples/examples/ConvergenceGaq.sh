#!/bin/bash


################CONVERGENCE SCRIPT#################                                                                            
#Convergence.sh

rm -f ./listcovergence.txt # gibbs energies of non-G286
rm -f ./listfails.txt     #List of fails to converge, or errors
rm -f ./Data.txt #List of grepped "Convergence" incidents
rm -f ./temp1.txt #Collected - fails (Convergence values)
rm -f ./temp2.txt #Collected - fails (Molecule name)
rm -f ./temp3.txt #Collected - fails  (counter, i)
rm -f ./temp4.txt #Reason for failure
rm -f ./temp5.txt #Collected MoleculenameSolventname
rm -f ./temp6.txt #list of molecules with pwd's
rm -f ./temp7.txt
rm -f ./error1.txt  #error counter text
rm -f ./error2.txt  #error molecule name text
rm -f ./error3.txt  #error pwd list
rm -f ./Errors.txt
#Grel only

rm -f .water_convergence.txt #Final Product, transfer energies of G286 (water)
rm -f .solvent_convergence.txt #Final Product, transfer energies of G286 (solvents)
rm -f ./temp5water.txt #Collected FilenameSolventname (water)
rm -f ./temp5solvent.txt #Collected FilnameSolventname (solvents)

i=1
j=1

#Checking format.awk to see if we are dealing with gas phase or PCM calculations

FOLDER=`pwd | awk 'BEGIN { FS = "/" } ; {printf("%s\n",$6)}'`

 echo "FOLDER: $FOLDER"

rm -f .ENERGY_$FOLDER.txt
rm -f HydENERGY_$FOLDER.txt





#---------------------------------------Gaq && Gnonaq ---------------------------#
for Gdir in G* ; do
  \echo "Gdir: $Gdir"
  if [ $Gdir == "Gaq" ]; then  
    cd $Gdir
    for file in *.out ; do
	
	\echo "file: $file"
        
	#Obtaining the free energy in which the calculation has convered to. $ENERGY will dump into final energy output    
	
	ENERGY=`grep Convergence $file | tail -n 1 | awk '{printf ($2 "\n")}'`
	#Information Gathering

	molecule=`ls $file|sed ' s/.out// '` 		#Obtains molecule name        
	echo $molecule >> ../temp2.txt                #Relays the file name to temp2.txt, the file name list  
        grep "Convergence" $file >> ../temp1.txt      #Obtains the Convergence line to add to temp1 (if it doesn't exist, grep1 handles it)
        echo $i >> ../temp3.txt                       #Relays Counter $i to temp3.txt, the counter list	
	echo $molecule$solvent >> ../temp5.txt        #Relays our specific naming system (FilenameSolvent) to temp5.txt, the FileSolvent list
        echo `pwd`/$molecule >> ../temp6.txt          #Relays the location to temp6.txt, the pwd list
	


	#Fail Greps
	
	check=0						 #initializing check variable to 0, where  0=success
	grep1=`grep -c "Convergence" $file`		#Checking to see if convergence was reached
        grep2=`grep -c "failure" $file`   		#Checking to see if failure to converge occurred
	grep3=`grep -c "Q-Chem" $file` 			#Checking to see if file even has any contents!
        grep4=`grep -c "Q-Chem fatal error occurred in module scfman.C" $file`    #Checking to see if SCF cycles ran out
        grep5=`grep -c "Q-Chem fatal error occurred in module NewQAlloc.C" $file` #Checking to see if memory ran out

	#Fail Checks

	if [ $grep1 -eq 0 ]; then
		check=1	#No convergence grepped
		echo "Convergence Failed to Grep" >> ../temp1.txt #Handles the grepped Convergence list so that it is not offset
 	fi
	
	if [ $grep2 -lt 0 ]; then
		check=2	#Failure grepped
	fi
	
	if [ $grep3 -eq 0 ]; then
		check=3 #No Q-chem grepped
	fi

	
        #Error Reporting
	
	if [ $check -gt 0 ]; then
	   echo $i >> ../error1.txt
	   echo `pwd`/$file >> ../error3.txt 

           if [ $check -eq 1 ]; then
		               
		if [ $grep5 -gt 0 ]; then
		   echo "MEMORY (ALLOCATED MEMORY EXCEEDED)" >> ../temp4.txt
                else
                   echo "CONVERGENCE (NO Convergence GREPPED)" >> ../temp4.txt #Relays reason of failure to temp4.txt, fail reason list   
                fi
            fi
                
	    if [ $check -eq 2 ]; then
                     
		if [ $grep4 -gt 0 ]; then
                   echo "SCF (SCF MAX CYCLES REACHED)" >> ../temp4.txt
                else
                   echo "FAILURE (GREPPED failure)" >> ../temp4.txt             #Relays reason of failure to temp4.txt, fail reason list
                fi
            fi
                  
	    if [ $check -eq 3 ]; then
               echo "FILE (NO Q-chem GREPPED)" >> ../temp4.txt         #Relays reasons of failure to temp4.txt, fail reason list
            fi
	fi
	      
		
	
	i=`echo $i + 1 | bc `   #Number of total files
		
		if [ $check -eq 0 ]; then
		  j=`echo $j + 1 | bc ` #Number of successful files, must pass all grepchecks to +1
                  echo "ENERGY=$ENERGY"
		  echo $ENERGY >> ../.ENERGY_$FOLDER.txt	#FINAL RESULT DESIRED (ASIDE FROM TRANSFER ENERGIES)
	          echo $molecule$solvent >> ../temp7.txt        #Relays our specific naming system to temp7.txt for final ENERGY_$FOLDER.txt 
	        fi


    done #for file in *.out
 
    cd ../ #Leaving $Gdir 
 
  fi	 #if [ $Gdir != Grel ] 

done     #for Gdir in G*
#-------------------------------

\echo "---------{End of Script Things} -----------"

#End of script stuff
#----------------------------------------------------------------------------------------

#Counter Correction
i=`echo $i - 1 | bc `
j=`echo $j - 1 | bc `

#GAS 

paste temp7.txt ./.ENERGY_$FOLDER.txt > ./ENERGY_$FOLDER.txt


#PCM
#if [ $pcm -gt 0 ]; then
#	#FOR ALL EXCEPT G286
#	#paste temp5.txt listconvergence.txt > .UnsortedEnergies.txt
#	#FOR G86
#	paste temp5water.txt .water_convergence.txt > .UnsortedEnergies_W.txt
#	paste temp5solvent.txt .solvent_convergence.txt > .UnsortedEnergies_S.txt
#	paste .UnsortedEnergies_S.txt .UnsortedEnergies_W.txt | awk '{printf("%30s %20.10f\n",$1, 627.50947*($2 - $4))}' > .temp
#	sort .temp > ENERGY_$FOLDER\_TRANSFER.txt
#fi 

#Errors
if [ $i -gt $j ]; then
   paste  error1.txt error3.txt temp4.txt >> Errors.txt
   cp ../MasterErrors.txt ../.mastertemp.txt
   awk -vFOLDER=$FOLDER 'match($0,FOLDER) == 0 {print $0}' ../.mastertemp.txt > ../MasterErrors.txt
   cat ./Errors.txt >> ../MasterErrors.txt
fi

#Data
paste temp3.txt temp5.txt temp1.txt temp6.txt > Data.txt


#grep "failure" ./Data.txt > listfails.txt
#paste temp5.txt temp6.txt > pwdlist.txt


echo "Total Number of successful outputs: " $j
echo "Total Number of outputs grepped: " $i
#expect 3066 for pcm
#expect 2780? for gas


#REMOVING SHIT


rm -f ./temp1.txt #Collected - fails (Convergence values)
rm -f ./temp2.txt #Collected - fails (Molecule name)
rm -f ./temp3.txt #Collected - fails  (counter, i)
rm -f ./temp4.txt #Overwritten Convergence values
rm -f ./temp5.txt #Collected MoleculenameSolventname
rm -f ./temp6.txt #list of molecules with pwd's
rm -f ./error1.txt  #error counter text
rm -f ./error2.txt  #error molecule name text
rm -f ./error3.txt  #error pwd list

#G286 only

rm -f .water_convergence.txt #Final Product, transfer energies of G286 (water)
rm -f .solvent_convergence.txt #Final Product, transfer energies of G286 (solvents)
rm -f ./temp5water.txt #Collected FilenameSolventname (water)
rm -f ./temp5solvent.txt #Collected FilnameSolventname (solvents)
