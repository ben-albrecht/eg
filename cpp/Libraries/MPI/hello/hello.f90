program hello
  use mpi
  implicit none
  
  integer :: ierr ! return flag of MPI calls
  integer :: rank ! unique processor rank
  integer :: size ! total number of MPI processes
  
  call MPI_Init( ierr )
  if ( ierr .ne. MPI_SUCCESS ) then
     print *, "Error starting MPI.  Aborting."
     call MPI_ABORT( MPI_COMM_WORLD, ierr, ierr )
  end if
  
  call MPI_COMM_RANK( MPI_COMM_WORLD, rank, ierr )
  call MPI_COMM_SIZE( MPI_COMM_WORLD, size, ierr )
  
  print *, "Hello from: ", rank, " of ", size

  call MPI_FINALIZE( ierr )

end program hello
