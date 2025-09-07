#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PointStamped, Point
from std_msgs.msg import Header

class Sender(object):
    """This node sends PointStamp data at 2Hz"""
    def __init__(self):
        rospy.init_node('send_point_location')
        self.header = Header(stamp=rospy.Time.now(), frame_id='odom')
        self.point = Point(1.0, 2.0, 0.0)

    def run(self):
        my_point_stamped = PointStamped(header=self.header, point=self.point)
        publisher = rospy.Publisher('/my_point_object', PointStamped, queue_size=10)
        r = rospy.Rate(2)
        while not rospy.is_shutdown():
            my_point_stamped.header.stamp = rospy.Time.now()
            publisher.publish(my_point_stamped)
            r.sleep()

if __name__=='__main__':
    node = Sender()
    node.run()
