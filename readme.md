## Installtion Notes

<pre>
Try to follw these steps

1 - Tenserflow and OpenCV installation (A)
2 - Make sure your Camera is working
3 - Install requirements.txt
4 - Face recognition library (B)

A: For Tenserflow and OpenCV installation and problems checkout this video  <a style="display: inline;" href="https://www.youtube.com/watch?v=vekblEk6UPc">Tenserflow and Opencv installation for Pi </a>
<a style="display: inline;" href="https://github.com/PINTO0309/Tensorflow-bin">Repo for matching  Python-Tenserflow on a Raspberry Pi- architecture</a>

B: For Face recognition library checkout this video  <a style="display: inline;" href="https://smartbuilds.io/installing-face-recognition-library-on-raspberry-pi-4/"> Face recognition library</a>

</pre>

Credit and Thanks to Electrical Engineer [Hussain Balhareth](https://www.linkedin.com/in/hussain-balhareth-0a05211ba) He did the bar training and he gave me the chance to work on this project, he also did troubleshooting and testing for libraries and hardware issues 

## Requirements.txt

<pre>

#-------Raspberry pi  ---------

# Common
# pip==22.0.4 
six==1.16.0
numpy==1.22.3

# CV2 Most already installed from "Installtion Notes" section Above
imutils ==0.5.3

#face-recognition        ==1.3.0
#face-recognition-models ==0.3.0
#tensorflow              ==2.7.0
#tensorflow-estimator    ==2.7.0
#keras                   ==2.7.0
#Keras-Preprocessing     ==1.1.2
# opencv-contrib-python   ==4.5.5.64
# opencv-python           ==4.5.5.64
# dlib                    ==19.23.1

# Probably needed if you're using the Pi Camera -> Remember usb Cameras are easier to deal with
# picamera == 1.13 -> If this doesn't work - Probably won't it's old and not for new Pis -> OsError libmmal.so
# Consider using <a style="display: inline;" href="https://Github.com/raspberrypi/picamera2">PiCamera2</a>- Currently you'll have to build it though 

# Not Sure
scipy      == 1.8.0
matplotlib ==3.5.1
# ------- Others -----------
# Pillow     == 9.1.0
# flatbuffers ==2.0
# Probably needed -> argparse
# For keyboard stuff -> pynput
#------------------- Pi end----------------------------
</pre>

