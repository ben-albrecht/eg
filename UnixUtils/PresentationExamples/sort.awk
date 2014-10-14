#!/bin/awk -f

# Feed this awk script your Final.dat and it will calculate MUEs by category and generate an output
# To do: Create Final.dat
# Make this compatible with Final.dat
# dG = MSD,  dG'  = QChem Calcs
# $1=filehandlesolvent
# $2=|dG - dG'|
# $3=dG
# $4=dG'
# $5=charge
# $6=type
# $7=solvent
# $8=area

function abs(num){
  if (num > 0.0) return num
  else return -num
}

BEGIN { 

# If OPT defined
    # If OPT = Neutral
    # If OPT = Ion
    # If OPT = Anion
    # If OPT = Cation
    # If OPT = AqIon
    # If OPT = NonAqIon
    # If OPT = AqNeutral
    # If OPT = NonAqNeutral
    # If OPT = Trans
# If OPT not defined, perform regular sort.awk

neutrals = 0;
i_neutrals = 0;
ions = 0;
i_ions = 0;
cations = 0;
i_cations = 0;
anions = 0;
i_anions = 0;
aqneutrals = 0;
i_aqneutrals = 0;
nonaqneutrals = 0;
i = nonaqneutrals = 0;
aqions = 0;
i_aqions = 0;
nonaqions = 0;
i_nonaqions = 0;
trans = 0;
i_trans = 0;
total = 0;
i_total = 0;
}

########################################################################################
{
  if (opt == ""){
      # opt is undefined, carry on
      #IF all absolute energies (if type == "abs")
      if ($6 == "abs") {
      
          #all neutrals (if charge == 0)
          if ($5 == 0)
          	{neutrals += abs($2);
          	 i_neutrals += 1;
          	 total += abs($2);
          	 i_total += 1;}
          
          #all ions (if charge != 0)
          if ($5 != 0)
          	{ions += abs($2);
          	 i_ions += 1;
          	 total += abs($2);
          	 i_total += 1;}
          
          #all cations (if charge > 0)
          if ($5 > 0)
                  {cations += abs($2);
                   i_cations += 1;}
          
          #all anions (if charge < 0)
          if ($5 < 0)
                  {anions += abs($2);
                   i_anions += 1;}
          
          #aq. neutrals (if solvent == "water" && charge == 0)
          if ($7 == "water" && $5 == 0)
          	{aqneutrals += abs($2);
          	 i_aqneutrals += 1;}
          
          #nonaq. neutrals (if solvent != "water" && charge == 0)
          if ($7 != "water" && $5 == 0)
                  {nonaqneutrals += abs($2);
                   i_nonaqneutrals += 1;}
          
          #aq. ions (if solvent == "water" && charge != 0)
          if ($7 == "water" && $5 != 0)
                  {aqions += abs($2);
                   i_aqions += 1;}
          
          #nonaq. ions (if solvent != "water" && charge != 0)
          if ($7 != "water" && $5 != 0)
              {nonaqions += abs($2);
               i_nonaqions += 1;}
      
      } #END if (type == "abs")
      
      #IF transfer energies (if type == "rel")
      if ($6 == "rel") 
      	{trans += abs($2);
      	 i_trans += 1;
               total += abs($2);
               i_total += 1;}		#END (if type == "rel")
  } else {
      if (opt == "Neutral"){
          #all neutrals (if charge == 0)
          if ($5 == 0) {
              print $0
          }
      }
      if (opt == "Ion"){
          if ($5 != 0){
              print $0
          }
      }
      if (opt == "Anion"){
          if ($5 < 0){
              print $0
          }
      }
      if (opt == "Cation"){
          if ($5 > 0){
              print $0
          }
      }
      if (opt == "AqNeutral"){
          if ($7 == "water" && $5 == 0){
              print $0
          }
      }
      if (opt == "NonAqNeutral"){
          if ($7 != "water" && $5 == 0){
              print $0
          }
      }
      if (opt == "AqIon"){
          if ($7 == "water" && $5 != 0){
              print $0
          }
      }
      if (opt == "NonAqIons"){
          if ($7 != "water" && $5 != 0){
              print $0
          }
      }
      if (opt == "Trans"){
          if ($6 == "rel"){
              print $0
          }
      }
  } 
}	# END awk brackets
########################################################################################

END {
if (opt == ""){
    if (i_neutrals > 0)
    {print "neutrals N:", i_neutrals;
    print "neutrals MUE:", neutrals/i_neutrals;}
    if (i_ions > 0) 
    {print "ions N:", i_ions;
    print "ions MUE:", ions/i_ions;}
    if (i_cations > 0)
    {print "cations N:", i_cations;
    print "cations MUE:", cations/i_cations;}
    if (i_anions > 0)
    {print "anions N:", i_anions;
    print "anions MUE:", anions/i_anions;}
    if (i_aqneutrals > 0)
    {print "aqneutrals N:", i_aqneutrals;
    print "aqneutrals MUE:", aqneutrals/i_aqneutrals;}
    if (i_nonaqneutrals > 0)
    {print "nonaqneutrals N:", i_nonaqneutrals;
    print "nonaqneutrals MUE:", nonaqneutrals/i_nonaqneutrals;}
    if (i_aqions > 0)
    {print "aqions N:", i_aqions;
    print "aqions MUE:", aqions/i_aqions;}
    if (i_nonaqions > 0)
    {print "nonaqions N:", i_nonaqions;
    print "nonaqions MUE:", nonaqions/i_nonaqions;}
    if (i_trans > 0)
    {print "trans N:", i_trans;
    print "trans MUE:", trans/i_trans;}
    #TOTAL
    print "TOTAL N:", i_total;
    print "TOTAL MUE:", total/i_total;
}

}
