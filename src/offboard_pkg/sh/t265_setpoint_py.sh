gnome-terminal --window -e 'bash -c " source ../../../devel/setup.bash;roslaunch offboard_pkg rs_t265.launch; exec bash"' \
--tab -e 'bash -c "sleep 15; source ../../../devel/setup.bash;rosrun offboard_pkg t265_to_mavros_py.py; exec bash"' \
--tab -e 'bash -c "sleep 16; ./ttyTHS0.sh; exec bash"' \
--tab -e 'bash -c "sleep 18; roslaunch mavros px4.launch; exec bash"' \
--tab -e 'bash -c "sleep 15; source ../../../devel/setup.bash;roslaunch offboard_pkg setpoint_py.launch; exec bash"' \
--window -e 'bash -c "sleep 25; rostopic echo /mavros/local_position/pose; exec bash"' \
--window -e 'bash -c "sleep 25; rostopic echo /mavros/state; exec bash"' \
