cmake_minimum_required(VERSION 3.12)
project(TaskOne)

set(CMAKE_CXX_STANDARD 14)

add_executable(TaskOne main.cpp network.cpp network.h server.cpp server.h program.cpp program.h message.h)