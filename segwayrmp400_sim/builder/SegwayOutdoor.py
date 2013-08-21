#! /usr/bin/env morseexec

from morse.builder import *

# set sim speed to 20 fps
#bpymorse.set_speed(25,0,0)

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
sick.translate(x=0.55, z=0.25)
sick.properties(Visible_arc = True)
sick.properties(resolution = 1.0)
sick.properties(scan_window = 270)
segway.append(sick)

# Append a Pose sensor
#pose = Pose()
#segway.append(pose)

odom = Odometry()
odom.add_stream('ros', child_frame_id='/robot/base_link')
segway.append(odom)


# Append a Wheel Encoder sensor
#encoders = Sensor('wheel_encoders')
#encoders.translate(z=vOff)
#encoders.rotate(z=zRot)
#segway.append(encoders)

# Append a GPS sensor
gps = GPS()
segway.append(gps)


segway.add_default_interface('ros')
segway.translate(z=vOff)
#segway.unparent_wheels()

barrel = PassiveObject('/Users/hododav/devel/is4s_morse_additions/blender/props/ConstructionBarriers.blend', 'barrel')
barrel.setgraspable()
barrel.translate(x=10, y=0.5)

barrier = PassiveObject('/Users/hododav/devel/is4s_morse_additions/blender/props/ConstructionBarriers.blend', 'barrier')
barrier.setgraspable()
barrier.translate(x=20)
barrier.rotate(z=1.57)


# Configure the environment
env = Environment('is4s/large_field.blend')
env.aim_camera([1.0470, 0, 0.7854])
