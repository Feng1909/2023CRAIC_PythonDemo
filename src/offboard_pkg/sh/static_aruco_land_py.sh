gnome-terminal --window -e 'bash -c " source ../../../devel/setup.bash;roslaunch offboard_pkg rs_t265.launch; exec bash"' \
--tab -e 'bash -c "sleep 15; source ../../../devel/setup.bash;rosrun offboard_pkg t265_to_mavros_py.py; exec bash"' \
--tab -e 'bash -c "sleep 5; source ../../../devel/setup.bash;roslaunch offboard_pkg usb_cam0.launch; exec bash"' \
--tab -e 'bash -c "sleep 10; source ../../../devel/setup.bash;roslaunch offboard_pkg aruco_det.launch; exec bash"' \
--tab -e 'bash -c "sleep 10; ./ttyTHS0.sh; exec bash"' \
--tab -e 'bash -c "sleep 10; roslaunch mavros px4.launch; exec bash"' \
--tab -e 'bash -c "sleep 15; source ../../../devel/setup.bash;rosrun offboard_pkg static_aruco_land_py.py; exec bash"' \
--window -e 'bash -c "sleep 25; rostopic echo /mavros/local_position/pose; exec bash"' \
--window -e 'bash -c "sleep 25; rostopic echo /mavros/setpoint_raw/local; exec bash"' \
--window -e 'bash -c "sleep 25; rostopic echo /mavros/state; exec bash"' \
