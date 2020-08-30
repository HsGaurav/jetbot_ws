#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64

def callback(data):
    speed = 10
    print(" linear x " + str(data.linear.x) + " linear y " + str(data.linear.y) + " linear z " + str(data.linear.z))
    print(" angular x " + str(data.angular.x) + " angular y " + str(data.angular.y) + " angular z " + str(data.angular.z))
    pub1 = rospy.Publisher('/joint1_velocity_controller/command', Float64, queue_size=1)
    # left wheel
    pub2 = rospy.Publisher('/joint2_velocity_controller/command', Float64, queue_size=1)
    # right wheel
    if data.linear.x >= 0.5:
        pub1.publish(speed)
        pub2.publish(speed)
    elif data.angular.z == 1:
        pub2.publish(speed)
    elif data.angular.z == -1:
        pub1.publish(speed)
    elif data.linear.x <= -0.5:
        pub1.publish(-speed)
        pub2.publish(-speed)
    else:
        pub1.publish(0)
        pub2.publish(0)

    
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/cmd_vel", Twist, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
