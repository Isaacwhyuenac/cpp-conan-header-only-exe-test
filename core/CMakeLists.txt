cmake_minimum_required(VERSION 3.15)
project(core CXX)

FILE(GLOB HEADERS include/*.h include/**/*.h)
FILE(GLOB SOURCES src/*.cpp src/**/*.cpp)

message(STATUS "HEADERS: ${HEADERS}")

get_target_property(common_LIB_INCLUDE_DIRS common INTERFACE_INCLUDE_DIRECTORIES)

set(core_build_include_dirs
        "${HEADERS}"
        "${common_LIB_INCLUDE_DIRS}")

include_directories(${core_build_include_dirs})
string(REPLACE ";" "$<SEMICOLON>" dirs "${core_build_include_dirs}")

add_library(core ${SOURCES})
#target_include_directories(core PUBLIC include)

message("CMAKE_CURRENT_SOURCE_DIR: ${CMAKE_CURRENT_SOURCE_DIR}")

target_include_directories(core SYSTEM INTERFACE
        "$<BUILD_INTERFACE:${dirs}>"
        "$<INSTALL_INTERFACE:$<INSTALL_PREFIX>/${CMAKE_INSTALL_INCLUDEDIR}>")

target_include_directories(core PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)

add_executable(core-exe src/core/main.cpp)
target_link_libraries(core-exe core)

install(TARGETS core-exe DESTINATION "."
        RUNTIME DESTINATION bin
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
)
#set_target_properties(core PROPERTIES PUBLIC_HEADER ${HEADERS})
install(TARGETS core PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})

