cmake_minimum_required(VERSION 3.5)

# Find python and Boost - both are required dependencies
#find_package(Boost COMPONENTS python REQUIRED)
project(hello)
# Without this, any build libraries automatically have names "lib{x}.so"
find_package(PythonLibs REQUIRED)
set(PYTHON_INCLUDE_DIRS /usr/include/Python3.10/)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")


# Add a shared module - modules are intended to be imported at runtime.
# - This is where you add the source files
add_executable(hello foobar.cpp)

target_include_directories(hello PUBLIC "${PYTHON_INCLUDE_DIRS}")
target_link_libraries(hello ${PYTHON_LIBRARIES})
