# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.12

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/bin/cmake

# The command to remove a file.
RM = /usr/local/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/nvidia/PythonDemo_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/nvidia/PythonDemo_ws/build

# Include any dependencies generated for this target.
include offboard_pkg/CMakeFiles/t265_to_mavros.dir/depend.make

# Include the progress variables for this target.
include offboard_pkg/CMakeFiles/t265_to_mavros.dir/progress.make

# Include the compile flags for this target's objects.
include offboard_pkg/CMakeFiles/t265_to_mavros.dir/flags.make

offboard_pkg/CMakeFiles/t265_to_mavros.dir/src/t265_to_mavros.cpp.o: offboard_pkg/CMakeFiles/t265_to_mavros.dir/flags.make
offboard_pkg/CMakeFiles/t265_to_mavros.dir/src/t265_to_mavros.cpp.o: /home/nvidia/PythonDemo_ws/src/offboard_pkg/src/t265_to_mavros.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/nvidia/PythonDemo_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object offboard_pkg/CMakeFiles/t265_to_mavros.dir/src/t265_to_mavros.cpp.o"
	cd /home/nvidia/PythonDemo_ws/build/offboard_pkg && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/t265_to_mavros.dir/src/t265_to_mavros.cpp.o -c /home/nvidia/PythonDemo_ws/src/offboard_pkg/src/t265_to_mavros.cpp

offboard_pkg/CMakeFiles/t265_to_mavros.dir/src/t265_to_mavros.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/t265_to_mavros.dir/src/t265_to_mavros.cpp.i"
	cd /home/nvidia/PythonDemo_ws/build/offboard_pkg && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/nvidia/PythonDemo_ws/src/offboard_pkg/src/t265_to_mavros.cpp > CMakeFiles/t265_to_mavros.dir/src/t265_to_mavros.cpp.i

offboard_pkg/CMakeFiles/t265_to_mavros.dir/src/t265_to_mavros.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/t265_to_mavros.dir/src/t265_to_mavros.cpp.s"
	cd /home/nvidia/PythonDemo_ws/build/offboard_pkg && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/nvidia/PythonDemo_ws/src/offboard_pkg/src/t265_to_mavros.cpp -o CMakeFiles/t265_to_mavros.dir/src/t265_to_mavros.cpp.s

# Object files for target t265_to_mavros
t265_to_mavros_OBJECTS = \
"CMakeFiles/t265_to_mavros.dir/src/t265_to_mavros.cpp.o"

# External object files for target t265_to_mavros
t265_to_mavros_EXTERNAL_OBJECTS =

/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: offboard_pkg/CMakeFiles/t265_to_mavros.dir/src/t265_to_mavros.cpp.o
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: offboard_pkg/CMakeFiles/t265_to_mavros.dir/build.make
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: /opt/ros/melodic/lib/libtf.so
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: /opt/ros/melodic/lib/libtf2_ros.so
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: /opt/ros/melodic/lib/libactionlib.so
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: /opt/ros/melodic/lib/libtf2.so
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: /opt/ros/melodic/lib/libimage_transport.so
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: /opt/ros/melodic/lib/libmessage_filters.so
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: /opt/ros/melodic/lib/libclass_loader.so
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: /usr/lib/libPocoFoundation.so
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: /usr/lib/aarch64-linux-gnu/libdl.so
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: /opt/ros/melodic/lib/libroscpp.so
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: /opt/ros/melodic/lib/libxmlrpcpp.so
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: /opt/ros/melodic/lib/libroslib.so
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: /opt/ros/melodic/lib/librospack.so
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: /usr/lib/aarch64-linux-gnu/libpython2.7.so
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: /usr/lib/aarch64-linux-gnu/libboost_filesystem.so
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: /usr/lib/aarch64-linux-gnu/libboost_program_options.so
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: /usr/lib/aarch64-linux-gnu/libtinyxml2.so
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: /opt/ros/melodic/lib/libcv_bridge.so
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: /usr/lib/aarch64-linux-gnu/libopencv_core.so.3.2.0
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: /usr/lib/aarch64-linux-gnu/libopencv_imgproc.so.3.2.0
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: /usr/lib/aarch64-linux-gnu/libopencv_imgcodecs.so.3.2.0
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: /opt/ros/melodic/lib/librosconsole.so
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: /opt/ros/melodic/lib/librosconsole_log4cxx.so
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: /opt/ros/melodic/lib/librosconsole_backend_interface.so
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: /usr/lib/aarch64-linux-gnu/liblog4cxx.so
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: /usr/lib/aarch64-linux-gnu/libboost_regex.so
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: /opt/ros/melodic/lib/libroscpp_serialization.so
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: /opt/ros/melodic/lib/librostime.so
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: /opt/ros/melodic/lib/libcpp_common.so
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: /usr/lib/aarch64-linux-gnu/libboost_system.so
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: /usr/lib/aarch64-linux-gnu/libboost_thread.so
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: /usr/lib/aarch64-linux-gnu/libboost_chrono.so
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: /usr/lib/aarch64-linux-gnu/libboost_date_time.so
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: /usr/lib/aarch64-linux-gnu/libboost_atomic.so
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: /usr/lib/aarch64-linux-gnu/libpthread.so
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: /usr/lib/aarch64-linux-gnu/libconsole_bridge.so.0.4
/home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros: offboard_pkg/CMakeFiles/t265_to_mavros.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/nvidia/PythonDemo_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable /home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros"
	cd /home/nvidia/PythonDemo_ws/build/offboard_pkg && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/t265_to_mavros.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
offboard_pkg/CMakeFiles/t265_to_mavros.dir/build: /home/nvidia/PythonDemo_ws/devel/lib/offboard_pkg/t265_to_mavros

.PHONY : offboard_pkg/CMakeFiles/t265_to_mavros.dir/build

offboard_pkg/CMakeFiles/t265_to_mavros.dir/clean:
	cd /home/nvidia/PythonDemo_ws/build/offboard_pkg && $(CMAKE_COMMAND) -P CMakeFiles/t265_to_mavros.dir/cmake_clean.cmake
.PHONY : offboard_pkg/CMakeFiles/t265_to_mavros.dir/clean

offboard_pkg/CMakeFiles/t265_to_mavros.dir/depend:
	cd /home/nvidia/PythonDemo_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/nvidia/PythonDemo_ws/src /home/nvidia/PythonDemo_ws/src/offboard_pkg /home/nvidia/PythonDemo_ws/build /home/nvidia/PythonDemo_ws/build/offboard_pkg /home/nvidia/PythonDemo_ws/build/offboard_pkg/CMakeFiles/t265_to_mavros.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : offboard_pkg/CMakeFiles/t265_to_mavros.dir/depend

