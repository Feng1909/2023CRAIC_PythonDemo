import rospy
import ObjectDetect
#from mavros_msgs.msg import
from nav_msgs.msg import Odometry
import sensor_msgs.msg
import math
import time



obj_detect = ObjectDetect.ObjectDetected(0.5,math.pi) 

rospy.init_node("demo", anonymous=True)

def LaserCallBack(data): 
    global obj_detect
    obj_detect.InputLidarData(data) 
    
    dist = obj_detect.GetYawObjDistance(0) 
    print("f",dist)
    dist = obj_detect.GetYawObjDistance(math.pi/2) 
    print("l",dist)
    dist = obj_detect.GetYawObjDistance(-math.pi/2) 
    print("r",dist)
    dist = obj_detect.GetYawObjDistance(math.pi) 
    print("b",dist)

def DronePoseCallBack(msg): 

    position = msg.pose.pose.position

    
    lines = obj_detect.GetObjMsg()  
    if(len(lines)==0):
        return
    print("lines",lines)
    x = msg.pose.pose.orientation.x
    y = msg.pose.pose.orientation.y
    z = msg.pose.pose.orientation.z
    w = msg.pose.pose.orientation.w

    position = msg.pose.pose.position
    yaw = math.atan2(2*(w*z + x*y),1-2*(z*z+ y *y))
    
    sin_t = math.sin(yaw)
    cos_t = math.cos(yaw)
    for line in lines:
        start_x = line[0][0]
        start_y = line[0][1]
        end_x = line[1][0]
        end_y = line[1][1]
        line[0][0] = start_x * cos_t + start_y *sin_t + position.x
        line[0][1] = start_y * cos_t - start_x*sin_t + position.y
        line[1][0] = end_x * cos_t + end_y *sin_t + position.x
        line[1][1] = end_y * cos_t - end_x*sin_t + position.y
    pass

time.sleep(4)


rospy.Subscriber("/scan",sensor_msgs.msg.LaserScan,LaserCallBack) 
rospy.Subscriber("/mavros/global_position/local",Odometry,DronePoseCallBack)#



rospy.spin()