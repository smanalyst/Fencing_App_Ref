# Fencing_App_Ref

<b>Horribly named, but, here it is!</b>

Essentially, this software is the start of an attempt to teach a neural network to ref fencing. 

Built on top of <b>OpenPose</b> and <b>Tensorflow</b>, this application is able to track both fencers' bodies throughout a bout. 

There is also a version that uses OpenNI and the Microsoft Kinect to do the same thing - that will eventually become the prod version.

For now, you'll need to do the following:

Set up the directory like so: <br>
Fencing_App_Ref<br>
| <br>
 --Code<br>
|<br>
 --Video<br>
|<br>
 --Images<br>
|<br>
 --openpose<br>
 
Then, compile openpose into its folder, and at the top of any python code, add that folder to your PATH. 
