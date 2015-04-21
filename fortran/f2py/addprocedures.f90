function addfunction(a, b)
    ! Functions return items, but take arguments by value

    ! Allow fortran to check that all types are explicitly declared
    implicit none

    ! Still need to declare types of arguments
    real :: a, b
    ! Need to declare return type
    real ::addfunction

    ! The variable named after function is the return
    addfunction = a + b

end function addfunction

subroutine addroutine(a, b, result)
    ! Subroutines return nothing, but take arguments by reference

    ! Allow fortran to check that all types are explicitly declared
    implicit none

    ! Still need to declare types of arguments
    ! Intent type declaration necessary for passing to f2py,
    ! but also good practice in general
    real, intent (in) :: a, b
    real, intent (out) :: result

    ! Modifying result here should modify it outside of the subroutine
    result = a + b

end subroutine addroutine

