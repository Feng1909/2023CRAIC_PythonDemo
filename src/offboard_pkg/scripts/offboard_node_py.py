#! /usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import State
from mavros_msgs.srv import CommandBool, CommandBoolRequest, SetMode, SetModeRequest

current_state = State()
cur_position = [0, 0, 0]

def state_cb(msg):
    global current_state
    current_state = msg

def pos_cb(msg):
    cur_position[0]=msg.pose.position.x;
    cur_position[1]=msg.pose.position.y;
    cur_position[2]=msg.pose.position.z;


if __name__ == "__main__":
    rospy.init_node("offb_node_py")

    HEIGHT = rospy.get_param('~height')
    AUTO_ARM_OFFBOARD = rospy.get_param('~auto_arm_offboard')

    state_sub = rospy.Subscriber("mavros/state", State, callback = state_cb)

    position_sub = rospy.Subscriber("/mavros/local_position/pose", PoseStamped, callback = pos_cb)

    local_pos_pub = rospy.Publisher("mavros/setpoint_position/local", PoseStamped, queue_size=10)

    rospy.wait_for_service("/mavros/cmd/arming")
    arming_client = rospy.ServiceProxy("mavros/cmd/arming", CommandBool)    

    rospy.wait_for_service("/mavros/set_mode")
    set_mode_client = rospy.ServiceProxy("mavros/set_mode", SetMode)


    # Setpoint publishing MUST be faster than 2Hz
    rate = rospy.Rate(20)

    # Wait for Flight Controller connection
    while(not rospy.is_shutdown() and not current_state.connected):
        rate.sleep()

    pose = PoseStamped()

    pose.pose.position.x = 0
    pose.pose.position.y = 0
    #pose.pose.position.z = 0.5
    pose.pose.position.z = HEIGHT

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

        #if((abs(cur_position[0])<0.1)and(abs(cur_position[1])<0.1)and(abs(cur_position[2]-0.5)<0.1)and((rospy.Time.now() - last_req)>rospy.Duration(5.0))):
        if((abs(cur_position[0])<0.1)and(abs(cur_position[1])<0.1)and(abs(cur_position[2]-HEIGHT)<0.1)and((rospy.Time.now() - last_req)>rospy.Duration(5.0))):
             pose.pose.position.x = 0.5
             pose.pose.position.y = 0
             pose.pose.position.z = 0.5
             last_req = rospy.Time.now()

        if((abs(cur_position[0]-0.5)<0.1)and(abs(cur_position[1])<0.1)and(abs(cur_position[2]-0.5)<0.1)and((rospy.Time.now() - last_req)>rospy.Duration(5.0))):
             set_mode_client.call(land_set_mode)
             if(set_mode_client.call(land_set_mode).mode_sent == True):
                 rospy.loginfo("land enabled")
                 offboard_flag = 1

        local_pos_pub.publish(pose)

        rate.sleep()


