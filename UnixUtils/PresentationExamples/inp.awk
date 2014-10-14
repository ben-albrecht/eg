#!/usr/bin/awk -f

BEGIN{
  i = 0;
}

{
 if(NR < molecule_mark){ 
  if(NR == dielec_mark){
    printf("\t" inp_opt" "dielec"\n")
  }
  else{
    print $0
  }
 }
}

END{
}
