#include <stdio.h>
#include <mpi.h>
#include <unistd.h>

int main( int narg, char **arg )
{

    //Initialize MPI, Identify processors, etc.
    int nprocs, rank;
    MPI_Init(&narg, &arg);
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);
    MPI_Comm_size(MPI_COMM_WORLD,&nprocs);

    MPI_Request req;
    MPI_Status status;
    int tag = 0;

    // Seed RNG
    srand((unsigned)time(NULL) + rank*nprocs);

    int iter = 0;

    // Barrier to be sure rank 0 reaches MPI_Recv() before any of the other nodes call MPI_Isend()
    MPI_Barrier(MPI_COMM_WORLD);

    if (rank == 0) {

        // Rank 0 (master node) waits for any of the nprocs-1 remaining nodes to finish
        MPI_Recv(&iter, 1, MPI_INT, MPI_ANY_SOURCE, MPI_ANY_TAG, MPI_COMM_WORLD, &status);

        // status.MPI_SOURCE is the source rank of the last message received
        printf("Proc %d wins! It reached iter = %d\n", status.MPI_SOURCE, iter);

    } else {
        for(;;) {

            // Each proc. sleeps for a random amount of time, at most 1 second
            // First proc to reach iter=10 wins
            usleep((double(rand()) / RAND_MAX) * 1000000);
            iter++;

            if (iter >= 10) break;;
        }

        printf("rank %d done\n", rank);
        MPI_Isend(&iter, 1, MPI_INT, 0, tag, MPI_COMM_WORLD, &req);
    }


    MPI_Finalize();
}
