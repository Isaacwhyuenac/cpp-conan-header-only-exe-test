cmake_minimum_required(VERSION 3.15)
project(my_algorithm CXX)

include(GNUInstallDirs)

add_subdirectory(common)
add_subdirectory(core)

#add_library(my_algorithm src/my_algorithm.cpp)
#target_include_directories(my_algorithm PUBLIC include)
#
#
#set_target_properties(my_algorithm PROPERTIES PUBLIC_HEADER "include/my_algorithm.h")
#install(TARGETS my_algorithm)
