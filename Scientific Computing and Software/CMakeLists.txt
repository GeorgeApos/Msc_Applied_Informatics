cmake_minimum_required(VERSION 3.28)
project(Scientific_Computing_and_Software C)

set(CMAKE_C_STANDARD 11)

add_executable(Scientific_Computing_and_Software first_assignment.h
        second_assignment.h
        main.c
        parallel_second_assignment.h)

target_link_libraries(Scientific_Computing_and_Software m)

find_package(OpenMP)
if(OpenMP_C_FOUND)
    target_link_libraries(Scientific_Computing_and_Software OpenMP::OpenMP_C)
endif()

find_package(MPI)
if(MPI_C_FOUND)
    target_link_libraries(Scientific_Computing_and_Software MPI::MPI_C)
endif()

target_link_libraries(Scientific_Computing_and_Software -fopenmp)