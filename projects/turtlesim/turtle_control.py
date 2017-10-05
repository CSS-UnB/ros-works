import rospy
from geometry_msgs.msg import Twist

pi = 3.14159265359

rospy.init_node ('set_vel')
pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size = 1)
rate = rospy.Rate(10) #Hertz

def waituntill (time, pub, vel_msg):
    now = rospy.get_time()
    finish = now + time

    while now < finish:
        #rospy.loginfo("loop")
        pub.publish(vel_msg)
        now = rospy.get_time()



def turn_90h (vel, pub):
    vel_msg = Twist()
    vel_msg.angular.z = vel
    time = (pi/2)/vel

    waituntill(time, pub, vel_msg)

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

    print('Digite o tamanho do lado:')
    n = 0
    n = input()

    fazquadrado(n)
