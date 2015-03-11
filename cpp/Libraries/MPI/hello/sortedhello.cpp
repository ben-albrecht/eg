#include <iostream>
#include <mpi.h>

int main( int argc, char* argv[] )
{

  int err;  // return flag of MPI calls
  int rank; // unique processor rank
  int size; // total number of MPI processes

  MPI_Status Stat;
  err = MPI_Init( &argc, &argv );
  if ( err != MPI_SUCCESS ) {
    std::cout << "Error starting MPI.  Aborting." << std::endl;
    MPI_Abort( MPI_COMM_WORLD, err );
  }

  int outmsg = 1;
  int inmsg;
  MPI_Comm_size( MPI_COMM_WORLD, &size );
  MPI_Comm_rank( MPI_COMM_WORLD, &rank );


  if (rank == 0){

    std::cout << "Hello from: " << rank << " of " << size << std::endl;
    MPI_Send(&outmsg,1,MPI_INT,rank+1,MPI_ANY_TAG,MPI_COMM_WORLD);

  } else if ( rank == size - 1) {

    // Blocking Receive - will wait until msg received
    MPI_Recv(&inmsg,1,MPI_INT, rank - 1,MPI_ANY_TAG,MPI_COMM_WORLD,&Stat);
    std::cout << "Hello from: " << rank << " of " << size << std::endl;

  }
  else {

    // Blocking Receive - will wait until msg received
    MPI_Recv(&inmsg,1,MPI_INT,rank - 1,MPI_ANY_TAG,MPI_COMM_WORLD,&Stat);
    std::cout << "Hello from: " << rank << " of " << size << std::endl;
    MPI_Send(&outmsg,1,MPI_INT,rank+1,MPI_ANY_TAG,MPI_COMM_WORLD);

  }

// MPI_Barrier() - wait until all processors reach this point (synchronization)
// MPI_Wtime() - returns time in seconds since arbitrary time (must take a time)


  MPI_Finalize();

  return 0;

}
