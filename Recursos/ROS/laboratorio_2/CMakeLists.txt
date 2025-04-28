cmake_minimum_required(VERSION 3.0.2)

# Name of this package
project(laboratorio_2)


## Compile as C++11, supported in ROS
# add_compile_options(-std=c++11)

##Find catkin macros and libraries
##if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
##is used, also find other catkin packages
#find_package(catkinREQUIRED)

find_package(catkin REQUIRED COMPONENTS
    rospy
    turtlesim
    roscpp
    geometry_msgs
)


catkin_python_setup()

#Declare our catkin package
catkin_package()

#Specify locations of header files
include_directories(
    ${catkin_INCLUDE_DIRS}
)

#Declare the executable, along with its sourcefiles.
#If there are multiple executables, use multiple copies of
#this line.

add_executable(hello src/hello.cpp)
add_executable(pubvel src/pubvel.cpp)
add_executable(subpose src/subpose.cpp)

#Specify libraries against which tolink.
#Again, this line should be copied for each distinct executable in the package
target_link_libraries(hello ${catkin_LIBRARIES})
target_link_libraries(pubvel ${catkin_LIBRARIES})
target_link_libraries(subpose ${catkin_LIBRARIES})


catkin_install_python(PROGRAMS
   scripts/pycontroller.py
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
