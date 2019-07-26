# conan-httplib
    
## Reuse the packages

### Basic setup

    $ conan install httplib/0.2.1@omaralvarez/public-conan

### Package basic test

    $ conan create . username/bintray-repo
    
## Example usage in a CMake-based project

### Conan and CMake files

* A sample from `conanfile.txt` in the root directory:
```
[requires]
httplib/0.2.1@omaralvarez/public-conan
...

[generators]
cmake
...
```

* The `CMakeLists.txt` at the root directory:
```cmake
cmake_minimum_required(VERSION 3.8)
project(project_name CXX)

if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release)
endif()

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

set(CMAKE_CXX_STANDARD 14)
...
```
* The `CMakeLists.txt` of a dependent target:
```cmake
...
add_executable(example example.cpp)
target_link_libraries(example ${CONAN_LIBS})
...
```

### Running Conan and CMake 

* First, add new remote pointing to the repository: 
```
conan remote add omaralvarez https://api.bintray.com/conan/omaralvarez/public-conan
```
* Change directory to the build location and run Conan installation:
```shell
conan install .. -s build_type=Release --build=missing
```
where the `..` points to the project root at the parent directory.
* Run CMake:
```shell
cmake ..
```
