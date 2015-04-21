program addNumbers
! FORmula TRANslating code (free-form)
! This program does what FORTRAN does best: adding numbers


! Allow fortran to check that all types are explicitly declared
implicit none


! Type declarations
real :: a, b, result

! Executable Statements
a = 12.0
b = 15.0
result = a + b

! * denotes printing to screen
print *, 'The total is ', result

! Fortran is full of brilliant features:
! Identifiers (variables, procedures, etc.) are case-insensitivite
! Identifiers can not be longer than 31 characters

print *, 'The total is ', Result

end program addNumbers
