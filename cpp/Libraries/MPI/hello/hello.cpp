#include <iostream>
#include <mpi.h>

int main( int argc, char* argv[] )
{

  int err;  // return flag of MPI calls
  int rank; // unique processor rank
  int size; // total number of MPI processes
  
  err = MPI_Init( &argc, &argv );
  if ( err != MPI_SUCCESS ) {
    std::cout << "Error starting MPI.  Aborting." << std::endl;
    MPI_Abort( MPI_COMM_WORLD, err );
  }
  
  MPI_Comm_size( MPI_COMM_WORLD, &size );
  MPI_Comm_rank( MPI_COMM_WORLD, &rank );

  std::cout << "Hello from: " << rank << " of " << size << std::endl;

  MPI_Finalize();

  return 0;

}
