import rospy
from geometry_msgs.msg import Twist
import math

pi = 3.14159265359

rospy.init_node ('set_vel')
pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size = 1)
rate = rospy.Rate(10) #Hertz

def theta_to_rad (theta):
    rad = theta*pi/180
    return rad

def waituntill (time, pub, vel_msg):
    now = rospy.get_time()
    finish = now + time
    rate = rospy.Rate(10) #Hertz

    while now < finish:
        #rospy.loginfo("loop")
        pub.publish(vel_msg)
        now = rospy.get_time()
        rate.sleep()

def turn_90h (vel, pub):
    vel_msg = Twist()
    vel_msg.angular.z = vel
    time = (pi/2)/vel

    waituntill(time, pub, vel_msg)

def turn_theta (theta, vel, pub):
    vel_msg = Twist()
    vel_msg.angular.z = vel
#    rad = 0
    #rad = theta_to_rad(theta)
    time = theta/vel

    waituntill(time, pub, vel_msg)
    stop(pub)

def stop(pub):
    vel_msg = Twist()
    pub.publish(vel_msg)

def move_linear(vel, dist, pub):
    vel_msg = Twist()
    vel_msg.linear.x = vel
    time = dist/vel
    waituntill(time, pub, vel_msg)

def fazquadrado (lado):
    i = 0

    while i<4:
        move_linear(1.0, lado, pub)
        stop(pub)
        if (i < 3):
            turn_90h(1.0, pub)
        i = i+ 1

    print('Pronto')



while not rospy.is_shutdown():

    vel = 12
    print('Digite o valor de x e de y')
    x = 0
    x = input()

    y = 0
    y = input()

    dist = math.sqrt(x*x + y*y)
    theta = math.atan2(y,x)

    print(dist,' ', theta)

    turn_theta(theta, vel, pub)


    #fazquadrado(n)
