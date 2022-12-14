#!/usr/bin/env python3

import rospy
import cv_bridge
from cv_bridge import CvBridge
import numpy as np
from sensor_msgs.msg import Image
import cv2 


rospy.set_param('local_img_pub',{"path":"/home/aditya/catkin_ws/src/imagepub/src/sample_img.jpg","frequency":1})

br=CvBridge()



def publish():
    rospy.init_node('file_publisher',anonymous=True)


    path=rospy.get_param('local_img_pub/path')
    img=cv2.imread(path)
   

    freq=rospy.get_param('local_img_pub/frequency')
    rate=rospy.Rate(freq)
    pub=rospy.Publisher('image',Image,queue_size=10)

    msg=br.cv2_to_imgmsg(img)
    
    
    
    pub.publish(msg)
    rospy.loginfo('publishing the local image.....')
    rate.sleep
    	

if __name__ == '__main__':

  while not rospy.is_shutdown():
    publish()
    

