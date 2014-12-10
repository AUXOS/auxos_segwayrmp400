cmake_minimum_required(VERSION 2.8.3)
project(segway_joy_teleop)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS geometry_msgs rospy sensor_msgs libsegwayrmp440)

###################################################
## Declare things to be passed to other projects ##
###################################################

## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES joy_to_twist
  CATKIN_DEPENDS geometry_msgs rospy sensor_msgs libsegwayrmp440
#  DEPENDS system_lib
)


#############
## Install ##
#############

# Mark executable scripts (Python etc.) for installation
# not required for python when using catkin_python_setup()
install(PROGRAMS
  scripts/segway_joy_teleop.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)


# Mark other files for installation (e.g. launch and bag files, etc.)
install(FILES
  launch/teleop.launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

#############
## Testing ##
#############

## Add folders to be run by python nosetests
# catkin_add_nosetests(test)
