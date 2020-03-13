#!/usr/bin/env python
import os
import rospy
from duckietown import DTROS
from std_msgs.msg import String
from duckietown_msgs.msg import WheelsCmdStamped, BoolStamped

class MyNode(DTROS):   

	def __init__(self, node_name):        # initialize the DTROS parent class        
		super(MyNode, self).__init__(node_name=node_name)        # construct publisher        
		self.pub = rospy.Publisher('chatter', String, queue_size=10)   
		self.wheelsCnt = self.publisher('/duckiebot5/wheels_driver_node/wheels_cmd', WheelsCmdStamped, queue_size=1) 
	def run(self):        # publish message every 1 second        
		 #rate = rospy.Rate(1) # 1Hz        
		while not rospy.is_shutdown(): 
			msg = WheelsCmdStamped()
			msg.header.stamp = rospy.get_rostime()
			msg.vel_left = 0.1
			msg.vel_right = 0.2
			self.wheelsCnt.publish(msg)
			# sleep for 10 seconds
			rospy.sleep(2.)
			msg = WheelsCmdStamped()
			msg.header.stamp = rospy.get_rostime()
			msg.vel_left = 0.0
			msg.vel_right = 0.0  
			self.wheelsCnt.publish(msg)
			onShutdown()

if __name__ == '__main__':    # create the node    
	node = MyNode(node_name='my_node')    # run node    
	node.run()    # keep spinning    
	rospy.spin()