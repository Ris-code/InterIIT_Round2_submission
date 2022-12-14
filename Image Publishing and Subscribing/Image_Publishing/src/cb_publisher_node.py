#!/usr/bin/python3

import rospy 
from sensor_msgs.msg import Image 
from cv_bridge import CvBridge
import cv2
import numpy as np




rospy.init_node('cb_publisher', anonymous=True)

rospy.set_param('checker_img',{'width':5,'height':5,'square_size':1,'frequency':1})




def publish_message():
 

  pub = rospy.Publisher('cb_img', Image, queue_size=10)
    
  br = CvBridge()  

  
  freq=rospy.get_param('checker_img/frequency')
  rate = rospy.Rate(freq) 

  #sample_np_array=np.full(shape=(4,4,1),fill_value=255,dtype='uint8')

  width=rospy.get_param('checker_img/width')
  height=rospy.get_param('checker_img/height')
  size=rospy.get_param('checker_img/square_size')
 
 
  dark=0
  light=255
  present_color1=dark
  
  np_img_array=np.zeros((height,width),dtype=np.uint8)

  for i in range(height//size):
    if present_color1==dark:
        present_color1=light
    else:
        present_color1=dark    
    
    present_color2=present_color1
    for j in range(width//size):

      try:

        np_img_array[i*size:(i+1)*size,j*size:(j+1)*size]=np.full((size,size),present_color2,dtype=np.uint8)
        if present_color2==dark:
            present_color2=light
        else:
            present_color2=dark   
            
            
      except:
          pass
          print("exception")

  np_img_reshaped=np.reshape(np_img_array,(width*height))


  msg=Image()
  msg.header.seq=0
  msg.header.frame_id=''
  msg.height=height
  msg.width=width
  msg.encoding="8UC1"
  msg.is_bigendian=0
  msg.step=width
  msg.data=tuple(np_img_reshaped)

  


  
  rospy.loginfo(f'publishing image ')
        
  #cv2_ros=br.cv2_to_imgmsg()

  pub.publish(msg)
  #print(type(msg.data))
  rate.sleep
         

if __name__ == '__main__':
  while not rospy.is_shutdown():
    publish_message()



