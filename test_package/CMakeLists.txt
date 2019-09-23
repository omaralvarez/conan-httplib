project(PackageTest CXX)
cmake_minimum_required(VERSION 3.7)

set(CMAKE_CXX_STANDARD 11)
set(THREADS_PREFER_PTHREAD_FLAG ON)

find_package(Threads REQUIRED)

if(WITH_OPENSSL)
    add_definitions(-DCPPHTTPLIB_OPENSSL_SUPPORT)
endif(WITH_OPENSSL)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(example main.cpp)
target_link_libraries(example Threads::Threads ${CONAN_LIBS})