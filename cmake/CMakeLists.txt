cmake_minimum_required (VERSION 2.6)
project (Tutorial)

# Should we use our own math functions?
option (USE_MYMATH
        "Use tutorial provided math implementation" ON)

# The version number.
set (Tutorial_VERSION_MAJOR 1)
set (Tutorial_VERSION_MINOR 0)

# Configure a header file to pass some CMake settings to source
configure_file (
  "${PROJECT_SOURCE_DIR}/TutorialConfig.h.in"
  "${PROJECT_BINARY_DIR}/TutorialConfig.h"
)


# add the binary tree to the search path for include files
# so that we will find TutorialConfig.h
include_directories("${PROJECT_BINARY_DIR}")
include_directories ("${PROJECT_SOURCE_DIR}/MathFunctions")
add_subdirectory (MathFunctions)

# Add the executable
add_executable(Tutorial tutorial.cxx)
target_link_libraries (Tutorial MathFunctions)
