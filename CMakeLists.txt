################################################################
#   Top level CMakeLists.txt file for the AUXOS Common Project
################################################################


CMAKE_MINIMUM_REQUIRED(VERSION 2.6 FATAL_ERROR)

PROJECT(auxos_common)

# GO FORTH!
SUBDIRS(dubins_path_planning)
SUBDIRS(dubins_path_following)
