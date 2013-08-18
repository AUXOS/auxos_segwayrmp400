#! /usr/bin/env morseexec

from morse.builder import *
from is4s_morse_additions.builder import *

# set sim speed to 20 fps
bpymorse.set_speed(25,0,0)

vOff=0.3
#zRot=math.pi/2 # correct for vehicle axis being y-forward
zRot=0

# Append ATRV robot to the scene
segway = SegwayRMP400()

# Append an actuator
motion = MotionVWDiff()
segway.append(motion)
#motion.configure_modifier('NED')


# Append an IMU sensor
imu = IMU()
imu.translate(z=0.05)
segway.append(imu)

# append a lidar
sick = Sick()
sick.translate(x=0.55, z=0.3)
sick.properties(Visible_arc = True)
sick.properties(resolution = 1.0)
sick.properties(scan_window = 180)
segway.append(sick)

# Append a Pose sensor
#pose = Pose()
#segway.append(pose)

odom = Odometry()
segway.append(odom)
odom.add_stream('ros', child_frame_id='/robot/base_link')

# Append a Wheel Encoder sensor
#encoders = Sensor('wheel_encoders')
#encoders.translate(z=vOff)
#encoders.rotate(z=zRot)
#segway.append(encoders)

# Append a GPS sensor
gps = GPS()
segway.append(gps)
#camera = VideoCamera()
#camera.translate(x=0.4, z=0.37);
#camera.properties(cam_width=640)
#camera.properties(cam_height=480)
#segway.append(camera);

#trailer_camera = VideoCamera()
#trailer_camera.translate(x=-0.35, z=0.37);
#trailer_camera.rotate(x=3.14);
#trailer_camera.properties(cam_width=640)
#trailer_camera.properties(cam_height=480)
#segway.append(trailer_camera);

#follow_camera = VideoCamera()
#follow_camera.translate(x=-12, z=4);
#follow_camera.rotate(y=0.3);
#follow_camera.properties(cam_width=640)
#follow_camera.properties(cam_height=480)
#segway.append(follow_camera);


hitch=Sensor('hitch.blend')
hitch.translate(x=-0.56)
segway.append(hitch)

trailer = DualEm61Trailer()
coils=trailer.add_coils()
coils[0].add_stream('ros', 'is4s_morse_additions.middleware.ros.em61.EmDataPublisher')
coils[1].add_stream('ros', 'is4s_morse_additions.middleware.ros.em61.EmDataPublisher')

trailer_odom = Odometry()
trailer_odom.name="odom"
trailer_odom.translate(x=-2.35)
trailer.append(trailer_odom)
trailer_odom.add_stream('ros', child_frame_id='/trailer/base_link')


trailer.translate(x=-0.58, z=0.4)

trailer.attach_to(hitch)
trailer.add_default_interface('ros')


segway.add_default_interface('ros')
segway.translate(z=vOff)
#segway.unparent_wheels()

barrel = PassiveObject('/Users/hododav/Downloads/barrel.blend', 'barrel')
barrel.setgraspable()
barrel.translate(x=15, y=0, z=-0.1)

# Configure the environment
env = Environment('is4s/large_field.blend')
#env = Environment('land-1/trees')

env.aim_camera([1.0470, 0, 0.7854])
