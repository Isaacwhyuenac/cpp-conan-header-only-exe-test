cmake_minimum_required(VERSION 3.15)
project(common CXX)

#find_package(spdlog REQUIRED)

file(GLOB HEADERS include/*.h include/**/*.h)

message(STATUS "HEADERS: ${HEADERS}")

add_library(common INTERFACE)
add_library(my_algorithm::common ALIAS common)

target_link_libraries(common INTERFACE spdlog::spdlog)

target_include_directories(
        common INTERFACE $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>)

install(DIRECTORY ${PROJECT_SOURCE_DIR}/include/
        DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})

#install(DIRECTORY ${PROJECT_SOURCE_DIR}/include/
#        DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})