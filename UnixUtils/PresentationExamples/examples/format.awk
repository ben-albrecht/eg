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
  for(j = 1; j <= NF; j++){

    if($j == "DIELEC"){
    DIELEC = $(j+2)
    }

    if($j == "DIELEC="){
    DIELEC = $(j+1)
    }

  }


}

END{

printf("$rem\n")
printf("jobtype                 sp\n")
printf("basis                   6-31+G*\n")
printf("exchange                b3lyp\n")
printf("solvent_method          pcm\n")
printf("make_cube_files         true\n")
printf("MAX_SCF_CYCLES 100\n")
printf("$end\n\n")

printf("$pcm\n")
printf("Theory          CPCM\n")
printf("Method          PC-SWIG\n")
printf("Solver          Inversion\n")
printf("SurfaceType     4\n")
printf("Resolution      1.0\n")
printf("DensityThresh   0.001   ! Recommended density threshold value\n")
printf("IsoElecConv     0.001   ! about 0.63 kcal/mol\n")
printf("IsoElecMaxIter  20\n")
printf("$end\n\n")

printf("$plots\n")
printf("for isosurface\n")
printf("11 -5.0 5.0\n")
printf("11 -5.0 5.0\n")
printf("11 -5.0 5.0\n")
printf("0 1 0 0\n")
printf("0\n")
printf("$end\n\n")

printf("$pcm_solvent\n")
printf("Dielectric %f\n", DIELEC)
printf("$end\n\n")

#printf("MEM_TOTAL 4000\n")

printf("$molecule\n")

printf("%d %d\n", charge, mult)

for(j = 0; j < i; j++){
  
  printf("%d %10.6f %10.6f %10.6f\n", atnum[j], x[j], y[j], z[j]);

  }

printf("$end\n\n")

}
