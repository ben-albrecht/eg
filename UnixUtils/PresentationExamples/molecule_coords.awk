#!/usr/bin/awk -f

BEGIN{
  i = 0;
}

{
  if(NR == 7){
  charge = $1;
  mult = $2;
  }
  if(NR > 7 && NF == 4){
  atnum[i] = $1;
  x[i] = $2;
  y[i] = $3;
  z[i] = $4;
  i++;
  }
}

END{
 printf("$molecule\n")
 printf("%d %d\n", charge, mult)
 for(j = 0; j < i; j++){
   printf("%d %10.6f %10.6f %10.6f\n", atnum[j], x[j], y[j], z[j]);
 }
 printf("$end\n\n")
}
