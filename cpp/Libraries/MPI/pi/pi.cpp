#include <iostream>
#include <cstdlib>
#include <stdlib.h>
#include <cmath>
#include <mpi.h>

const double PI = 3.14159265359;

double urand()
{
  return rand() / static_cast<double>( RAND_MAX );
}

int main( int argc, char* argv[] )
{

  int size, rank, err;
  err = MPI_Init( &argc, &argv );
  if ( err != MPI_SUCCESS ) {
    std::cout << "Error starting MPI.  Aborting." << std::endl;
    MPI_Abort( MPI_COMM_WORLD, err );
  }

  MPI_Comm_size( MPI_COMM_WORLD, &size );
  MPI_Comm_rank( MPI_COMM_WORLD, &rank );

  MPI_Barrier (MPI_COMM_WORLD);
  double start_time = MPI_Wtime();
  // get number of samples from command line
  int N = atoi( argv[1] );

  int Nproc = N / size; // N per processor

  int ncircleproc = 0;

  srand(time(NULL)*(rank+1));



  // Loop over Nproc for each process
  for ( int i=0; i<Nproc; i++ ) {
    double x = urand();
    double y = urand();
    if ( ( x*x + y*y ) < 1 )
      ncircleproc++;

  }

  // Global ncircle
  int ncircle = 0;

  // Reduce result down to master thread
  MPI_Reduce (&ncircleproc,&ncircle,1,MPI_INT,MPI_SUM, 0, MPI_COMM_WORLD);

  MPI_Barrier (MPI_COMM_WORLD);

  // Master thread only
  if (rank == 0) {
    double pi = 4 * static_cast<double>(ncircle) / N;

    std::cout << "Pi estimation: " << pi << std::endl;
    std::cout << "Absolute error: " << std::abs( PI - pi ) << std::endl;
    std::cout << "Timing: " << MPI_Wtime() - start_time << std::endl;
  }

  MPI_Finalize();

  return 0;
}
