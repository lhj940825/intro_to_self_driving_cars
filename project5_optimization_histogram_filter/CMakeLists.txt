cmake_minimum_required(VERSION 3.22)
project(Project5)

set(CMAKE_CXX_STANDARD 17)


add_executable(HistogramOptimize optimized_code/main.cpp
                                 optimized_code/blur.cpp
                                 optimized_code/initialize_beliefs.cpp
                                 optimized_code/move.cpp
                                 optimized_code/normalize.cpp
                                 optimized_code/print.cpp
                                 optimized_code/sense.cpp
                                 optimized_code/zeros.cpp)

#add_executable(HistogramOptimize andy_histogram_filter/main.cpp
#                                    andy_histogram_filter/blur.cpp
#                                    andy_histogram_filter/initialize_beliefs.cpp
#                                    andy_histogram_filter/move.cpp
#                                    andy_histogram_filter/normalize.cpp
#                                    andy_histogram_filter/print.cpp
#                                    andy_histogram_filter/sense.cpp
#                                    andy_histogram_filter/zeros.cpp)
add_compile_options(-Wall -std=c++14 -O2 -fPIC)