cmake_minimum_required(VERSION 3.15)

project(try LANGUAGES CXX VERSION 1.2.3)

add_executable(trel file1.cpp)

add_executable(inoi file2.cpp)

add_executable(aqua file3.cpp)



##########################################################
###https://stackoverflow.com/questions/49018868/how-do-i-make-cmake-run-a-python-script-before-building-in-order-to-generate-fi
##########################################################

# ALL THE PREDEFINED CMake Modules ARE LOCATED HERE:
# /usr/share/cmake-3.22/Modules/
#find Python:
find_package(Python COMPONENTS Interpreter REQUIRED)

#from $cat /usr/share/cmake-3.22/Modules/FindPython.cmake :

#This module will set the following variables in your #project
#(see :ref:`Standard Variable Names <CMake Developer #Standard Variable Names>`):
#
#``Python_FOUND``
#  System has the Python requested components.
#``Python_Interpreter_FOUND``
#  System has the Python interpreter.
#``Python_EXECUTABLE``
#  Path to the Python interpreter.
#``Python_INTERPRETER_ID``
#  A short string unique to the interpreter. Possible #values include:

###!!! NO PYTHON_EXECUTABLE   !!!###
###!!! ONLY Python_EXECUTABLE !!!###

###ALWAYS CHECK IF Python IS FOUND OR NOT!!!###
if(Python_EXECUTABLE)
    message(STATUS "Found Python: ${Python_EXECUTABLE}")
else()
    message(STATUS "Found Python: Python NOT FOUND")
endif()

message("CMAKE_SOURCE_DIR=${CMAKE_SOURCE_DIR} Python=${Python} Python_INCLUDE_DIRS=${Python_INCLUDE_DIRS} PYTHON_EXECUTABLE=${Python_EXECUTABLE}")

#add_custom_command(TARGET last COMMAND
#"${PYTHON_EXECUTABLE}" "${CMAKE_SOURCE_DIR}/script.py")

execute_process(
   #COMMAND ${PYTHON_EXECUTABLE} script.py
    COMMAND ${Python_EXECUTABLE} "${CMAKE_SOURCE_DIR}/script.py"
    OUTPUT_VARIABLE RESULT
    OUTPUT_STRIP_TRAILING_WHITESPACE
)
message(STATUS "RESULT=${RESULT} CMAKE_SOURCE_DIR=${CMAKE_SOURCE_DIR} CMAKE_CURRENT_BINARY_DIR=${CMAKE_CURRENT_BINARY_DIR} PYTHON_EXECUTABLE=${Python_EXECUTABLE}")


# THIS IS CALLED ONLY WHEN YOU DO:
# #cmake .
# i. e. AT PRE BUILD TIME ONLY!!!
# MULTIPLE RUNS OF $make AND $make invain and $make all
# DO NOTHING!!!
add_custom_target(CreateFile
              COMMAND ${Python_EXECUTABLE} "${CMAKE_SOURCE_DIR}/script.py"
              BYPRODUCTS "${CMAKE_SOURCE_DIR}/myfile.txt"
              COMMENT "Running script.py..."
)





add_custom_command(OUTPUT "${CMAKE_SOURCE_DIR}/o.cpp"
    COMMAND ${Python_EXECUTABLE} "${CMAKE_SOURCE_DIR}/makecpp.py"
    #DEPENDS "${CMAKE_SOURCE_DIR}/file1.cpp"
    #WORKING_DIRECTORY "${CMAKE_SOURCE_DIR}"
    #COMMENT "CONSTRUCTING o.cpp..."
)

add_custom_target(makecpp #ALL
    DEPENDS "${CMAKE_SOURCE_DIR}/o.cpp")
#target_sources(makecpp PRIVATE  "${CMAKE_SOURCE_DIR}/onecpp.cpp")

#add_executable(onecpp "${CMAKE_SOURCE_DIR}/o.cpp")


#install(FILES ${CMAKE_CURRENT_BINARY_DIR}/include/Generated.hpp DESTINATION include)
