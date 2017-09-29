import rospy
from geometry_msgs.msg import Twist

pi = 3.14159265359

rospy.init_node ('set_vel')
pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size = 1)
rate = rospy.Rate(10) #Hertz



def turn_90h (vel, pub):
    vel_msg = Twist()
    vel_msg.angular.z = vel
    time = (pi/2)/vel

    pub.publish(vel_msg)
    rospy.sleep(time)

def stop(pub):
    vel_msg = Twist()
    pub.publish(vel_msg)

def move_linear(vel, dist, pub):
    vel_msg = Twist()
    vel_msg.linear.x = vel
    time = dist/vel

    pub.publish(vel_msg)
    rospy.sleep(time)


while not rospy.is_shutdown():

    turn_90h(1, pub)
    stop(pub)
    move_linear(1, 10, pub)
