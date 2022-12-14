i)The node image_changer node has subscribes to the image topic which is published by the file_publisher so its required to run that node simultaneously.

ii)For node image_changer it perhaps can't update itself to the rosparameters unless we comment the ros_set parametrs after running the file once as this would set the parameters and then while running this again this wouldn't overwrite the rosparameters which are given via terminal i.e., in every iteration it doesn't read the updated parameters so we have to re run the node this bug is yet to be corrected
