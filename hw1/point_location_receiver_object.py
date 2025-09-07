#!/usr/bin/env python3 

import rospy
from geometry_msgs.msg import PointStamped

class Receiver(object):
    """This node receives PointStamped data and prints it"""
    def __init__(self):
        rospy.init_node('receive_point_location')
        rospy.Subscriber('/my_point_object', PointStamped, self.process_point)
        rospy.spin()

    def process_point(self, data):
        print("[{:.2f}, {:.2f}, {:.2f}]".format(data.point.x, data.point.y, data.point.z))

if __name__ == '__main__':
    node = Receiver()
