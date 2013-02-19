#! /usr/bin/env morseexec

from morse.builder import *

vOff=0.3
#zRot=math.pi/2 # correct for vehicle axis being y-forward
zRot=0

# Append ATRV robot to the scene
segway = SegwayRMP400()
segway.unparent_wheels()

# Append an actuator
motion = MotionVWDiff()
segway.append(motion)
#motion.configure_modifier('NED')


# Append an IMU sensor
imu = IMU()
imu.translate(z=0.05)
segway.append(imu)


# Append a Pose sensor
pose = Pose()
segway.append(pose)

# Append a Wheel Encoder sensor
#encoders = Sensor('wheel_encoders')
#encoders.translate(z=vOff)
#encoders.rotate(z=zRot)
#segway.append(encoders)

# Append a GPS sensor
gps = GPS()
segway.append(gps)


segway.add_default_interface('ros')

# Configure the environment
env = Environment('is4s/large_field')
env.aim_camera([1.0470, 0, 0.7854])
