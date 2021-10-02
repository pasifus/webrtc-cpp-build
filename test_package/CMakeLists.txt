project(test_package CXX)
cmake_minimum_required(VERSION 3.11)

# force enable verbose mode
set(CMAKE_VERBOSE_MAKEFILE ON)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package(webrtc REQUIRED)

add_executable(${PROJECT_NAME} test_package.cpp)
target_link_libraries(${PROJECT_NAME} webrtc::webrtc)
set_property(TARGET ${PROJECT_NAME} PROPERTY CXX_STANDARD 14)