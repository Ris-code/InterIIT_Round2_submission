#!/usr/bin/python3


import rospy
import numpy as np
from sensor_msgs.msg import Image
from io import BytesIO

rospy.set_param('contrast_brightness',{'contrast':2,'brightness':2,'frequency':10})


class image_changer_node():
    def __init__(self,c,b,freq):
        
        rospy.init_node('image_changer',anonymous=True)
        
        self.c=c
        self.b=b
        self.freq=freq
        self.rate = rospy.Rate(freq) 

    def publish_image(self,changed_img_msg):

        #print(changed_img_msg)
        Publisher_=rospy.Publisher('Changed_image',Image,queue_size=10)

        Publisher_.publish(changed_img_msg)
        rospy.loginfo('publishing the changed image .....')
        

    def subscribe_image(self):
        
        rate=rospy.Rate(0.01)
        def call_back_sub(img_msg):
        
            #load_bytes = BytesIO(img_msg.data)
            #loaded_np = np.load(load_bytes, allow_pickle=True)
            array = np.array(np.frombuffer(img_msg.data, dtype=np.uint8))        
            #t=type(a)
            #rospy.loginfo(f"receiving the info ..... {t},   {a}")
            rospy.loginfo("receiving the info .....")

            ##changing the contrast


            msg1=np.array(array.data,dtype=float)

            msg_2=msg1*self.c+self.b
            changed_img_msg=img_msg
            img_data=np.array(np.clip(msg_2,0,255),dtype=np.uint8)
            #print(msg1)
            #print(img_data)
            #changed_img_msg.data=tuple(np.array(np.clip(msg_2,0,255),dtype=np.uint8))
            changed_img_msg.data=img_data.tobytes('C')

            self.publish_image(changed_img_msg)


        while not rospy.is_shutdown():
            rospy.Subscriber('image',Image,call_back_sub)
            rate.sleep()

if __name__ == '__main__':

 freq=rospy.get_param('contrast_brightness/frequency')
 b=rospy.get_param('contrast_brightness/brightness')        
 c=rospy.get_param('contrast_brightness/contrast')    
 node=image_changer_node(c,b,freq)
 node.subscribe_image()


 #while not rospy.is_shutdown():
 #   freq=rospy.get_param('contrast_brightness/frequency')
 #   b=rospy.get_param('contrast_brightness/brightness')        
 #   c=rospy.get_param('contrast_brightness/contrast') 
 #   node=image_changer_node(c,b,freq)
        



    
    

