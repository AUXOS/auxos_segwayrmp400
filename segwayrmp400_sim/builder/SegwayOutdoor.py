#! /usr/bin/env morseexec

from morse.builder import *

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


# Append a Pose sensor
#pose = Pose()
#segway.append(pose)

odom = Odometry()
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

# Configure the environment
env = Environment('is4s/large_field.blend')
env.aim_camera([1.0470, 0, 0.7854])
