#!/usr/bin/env python3
"""
This script published ROS messages containing the 3D coordinates of a single point
"""
import rospy
from geometry_msgs.msg import PointStamped, Point
from std_msgs.msg import Header

rospy.init_node('send_point_location')
my_header = Header(stamp=rospy.Time.now(), frame_id='odom')
my_point = Point(1.0, 2.0, 0.0)
my_point_stamped = PointStamped(header=my_header, point=my_point)

publisher = rospy.Publisher('/my_point', PointStamped, queue_size=10)
r = rospy.Rate(2)
while not rospy.is_shutdown():
    my_point_stamped.header.stamp = rospy.Time.now()
    publisher.publish(my_point_stamped)
    r.sleep()
