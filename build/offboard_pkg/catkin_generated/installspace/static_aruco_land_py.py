#!/usr/bin/env python2

import rospy
import os
import sys
#import numpy as np
import math
#from scipy.spatial.transform import Rotation as R
from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import State, PositionTarget
from mavros_msgs.srv import CommandBool, CommandBoolRequest, SetMode, SetModeRequest
from offboard_pkg.msg import ArucoInfo

current_state = State()
cur_position = [0, 0, 0]
position_det = [0, 0, 0]
aruco_pos_enu = [0, 0, 0]
cur_position_tempstore = [0, 0, 0]
#cur_position_x 
#cur_position_y 
#cur_position_z 
num_regain = 0
num_lost = 0
VISION_THRES = 13
state_flag = 0
is_detected = False
state20_count = 0
current_roll = 0
current_pitch = 0
current_yaw = 0

# https://www.lmlphp.com/user/221449/article/item/6812040/
def quaternion_to_euler(x, y, z, w):
    t0 = +2.0 * (w * x + y * z)
    t1 = +1.0 - 2.0 * (x * x + y * y)
    X = math.degrees(math.atan2(t0, t1))

    t2 = +2.0 * (w * y - z * x)
    t2 = +1.0 if t2 > +1.0 else t2
    t2 = -1.0 if t2 < -1.0 else t2
    Y = math.degrees(math.asin(t2))

    t3 = +2.0 * (w * z + x * y)
    t4 = +1.0 - 2.0 * (y * y + z * z)
    Z = math.degrees(math.atan2(t3, t4))

    return X, Y, Z


def state_cb(msg):
    global current_state
    current_state = msg

def pos_cb(msg):
    cur_position[0] = msg.pose.position.x;
    cur_position[1] = msg.pose.position.y;
    cur_position[2] = msg.pose.position.z;
    cur_Euler=quaternion_to_euler(msg.pose.orientation.x, msg.pose.orientation.y, msg.pose.orientation.z, msg.pose.orientation.w)
    current_roll = cur_Euler[0];
    current_pitch = cur_Euler[1];
    current_yaw = cur_Euler[2];


def aruco_det_cb(msg):
    global num_regain
    global num_lost
    global is_detected
    detected_1=msg.detected
    position_det[0] = msg.position[0]
    position_det[1] = msg.position[1]
    position_det[2] = msg.position[2]

    if(detected_1):
        num_regain = num_regain + 1
        num_lost = 0
    else:
        num_regain = 0
        num_lost = num_lost + 1

    if(num_lost > VISION_THRES):
        is_detected = False

    if(num_regain > VISION_THRES):
        is_detected = True


if __name__ == "__main__":
    rospy.init_node("offb_node_py")

    #HEIGHT = rospy.get_param('~height')
    #AUTO_ARM_OFFBOARD = rospy.get_param('~auto_arm_offboard')
    AUTO_ARM_OFFBOARD = False

    state_sub = rospy.Subscriber("mavros/state", State, callback = state_cb)

    position_sub = rospy.Subscriber("/mavros/local_position/pose", PoseStamped, callback = pos_cb)

    aruco_det_sub = rospy.Subscriber("/drone/object_detection/aruco_det", ArucoInfo, callback = aruco_det_cb)

    local_pos_pub = rospy.Publisher("mavros/setpoint_position/local", PoseStamped, queue_size=10)

    setpoint_raw_local_pub = rospy.Publisher("/mavros/setpoint_raw/local", PositionTarget, queue_size=10)

    rospy.wait_for_service("/mavros/cmd/arming")
    arming_client = rospy.ServiceProxy("mavros/cmd/arming", CommandBool)    

    rospy.wait_for_service("/mavros/set_mode")
    set_mode_client = rospy.ServiceProxy("mavros/set_mode", SetMode)


    # Setpoint publishing MUST be faster than 2Hz
    rate = rospy.Rate(20)

    # Wait for Flight Controller connection
    while(not rospy.is_shutdown() and not current_state.connected):
        rate.sleep()

    # if auto offboard,need to Send a few setpoints before starting
    if(AUTO_ARM_OFFBOARD == True):
        pose = PoseStamped()

        pose.pose.position.x = 0
        pose.pose.position.y = 0
        pose.pose.position.z = 0.5
        #pose.pose.position.z = HEIGHT

        # Send a few setpoints before starting
        for i in range(100):   
            if(rospy.is_shutdown()):
                break

            local_pos_pub.publish(pose)
            rate.sleep()

    offb_set_mode = SetModeRequest()
    offb_set_mode.custom_mode = 'OFFBOARD'

    land_set_mode = SetModeRequest()
    land_set_mode.custom_mode = 'AUTO.LAND'

    arm_cmd = CommandBoolRequest()
    arm_cmd.value = True

    offboard_flag = 0

    last_req = rospy.Time.now()

    while(not rospy.is_shutdown()):
        if(AUTO_ARM_OFFBOARD == True):
            if(current_state.mode != "OFFBOARD" and (rospy.Time.now() - last_req) > rospy.Duration(5.0) and (offboard_flag == 0)):
                if(set_mode_client.call(offb_set_mode).mode_sent == True):
                    rospy.loginfo("OFFBOARD enabled")

                last_req = rospy.Time.now()
            else:
                if(not current_state.armed and (rospy.Time.now() - last_req) > rospy.Duration(5.0) and (offboard_flag == 0)):
                    if(arming_client.call(arm_cmd).success == True):
                        rospy.loginfo("Vehicle armed")

                    last_req = rospy.Time.now()

        pos_setpoint = PositionTarget()

        if(state_flag == 0):
            pos_setpoint.type_mask = 0b100111111000  # 100 111 111 000  xyz + yaw
            pos_setpoint.coordinate_frame = 1
            pos_setpoint.position.x = 0
            pos_setpoint.position.y = 0
            pos_setpoint.position.z = 0.7
            pos_setpoint.yaw = 0
            setpoint_raw_local_pub.publish(pos_setpoint)
           
            if((abs(cur_position[0])<0.1)and(abs(cur_position[1])<0.1)and(abs(cur_position[2]-0.7)<0.1)and((rospy.Time.now() - last_req)>rospy.Duration(5.0))):
                state_flag = 1;
                time_snap1 = rospy.Time.now()


        if(state_flag == 1):
            pos_setpoint.type_mask = 0b100111111000  # 100 111 111 000  xyz + yaw
            pos_setpoint.coordinate_frame = 1
            pos_setpoint.position.x = 1
            pos_setpoint.position.y = 0
            pos_setpoint.position.z = 0.7
            pos_setpoint.yaw = 0
            setpoint_raw_local_pub.publish(pos_setpoint)
           
            if((abs(cur_position[0]-1)<0.1)and(abs(cur_position[1])<0.1)and(abs(cur_position[2]-0.7)<0.1)and((rospy.Time.now() - time_snap1)>rospy.Duration(5.0))):
                state_flag = 2;
                time_snap2 = rospy.Time.now()


        if(state_flag == 2):
            if(is_detected == False):
                state_flag = 20

            pos_setpoint.type_mask = 0b100111111000  # 100 111 111 000  xyz + yaw
            pos_setpoint.coordinate_frame = 1
            aruco_pos_enu[0] = cur_position[0] - position_det[1]
            aruco_pos_enu[1] = cur_position[1] - position_det[0]
            aruco_pos_enu[2] = cur_position[2] - position_det[2]
            print "aruco_pos_enu[0] is ", aruco_pos_enu[0]
            print "aruco_pos_enu[1] is ", aruco_pos_enu[1]
            print "aruco_pos_enu[2] is ", aruco_pos_enu[2]
            pos_setpoint.position.x = aruco_pos_enu[0]
            pos_setpoint.position.y = aruco_pos_enu[1]
            pos_setpoint.position.z = aruco_pos_enu[2] + 0.7
            pos_setpoint.yaw = 0
            setpoint_raw_local_pub.publish(pos_setpoint)
            if((abs(position_det[0]) < 0.05)and(abs(position_det[1]) < 0.05)): 
                state_flag = 3  

        
        if(state_flag == 3):  
            pos_setpoint.type_mask = 0b100111000100
            pos_setpoint.coordinate_frame = 1
            pos_setpoint.velocity.x = 0
            pos_setpoint.velocity.y = 0
            pos_setpoint.velocity.z = -0.1
            pos_setpoint.position.x = aruco_pos_enu[0]
            pos_setpoint.position.y = aruco_pos_enu[1]
            pos_setpoint.yaw = 0
            setpoint_raw_local_pub.publish(pos_setpoint)
            if(cur_position[2]  < 0.36):
                state_flag = 4;

        if(state_flag == 4):
            pos_setpoint.type_mask = 0b100111111000  # 100 111 111 000  xyz + yaw
            pos_setpoint.coordinate_frame = 1
            aruco_pos_enu[0] = cur_position[0] - position_det[1]
            aruco_pos_enu[1] = cur_position[1] - position_det[0]
            aruco_pos_enu[2] = cur_position[2] - position_det[2]
            print "aruco_pos_enu[0] is ", aruco_pos_enu[0]
            print "aruco_pos_enu[1] is ", aruco_pos_enu[1]
            print "aruco_pos_enu[2] is ", aruco_pos_enu[2]
            pos_setpoint.position.x = aruco_pos_enu[0]
            pos_setpoint.position.y = aruco_pos_enu[1]
            pos_setpoint.position.z = aruco_pos_enu[2] + 0.35
            pos_setpoint.yaw = 0
            setpoint_raw_local_pub.publish(pos_setpoint)
            if((abs(position_det[0]) < 0.05)and(abs(position_det[1]) < 0.05)): 
                state_flag = 10

        
     
        if(state_flag == 10):
            set_mode_client.call(land_set_mode)
            if(set_mode_client.call(land_set_mode).mode_sent == True):
                rospy.loginfo("land enabled")
                offboard_flag = 1

        if(state_flag == 20):
            state20_count = state20_count + 1
            if(state20_count == 1):
                cur_position_tempstore[0] = cur_position[0]
                cur_position_tempstore[1] = cur_position[1]
                cur_position_tempstore[2] = cur_position[2]
                current_yaw_tempstore = current_yaw
            pos_setpoint.type_mask = 0b100111111000  # 100 111 111 000  xyz + yaw
            pos_setpoint.coordinate_frame = 1
            pos_setpoint.position.x = cur_position_tempstore[0]
            pos_setpoint.position.y = cur_position_tempstore[1]
            pos_setpoint.position.z = cur_position_tempstore[2]
            pos_setpoint.yaw = current_yaw_tempstore
            setpoint_raw_local_pub.publish(pos_setpoint)
            if(is_detected == True):
                state_flag = 2
                state20_count = 0






        #local_pos_pub.publish(pose)

        rate.sleep()


