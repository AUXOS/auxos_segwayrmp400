from morse.builder.morsebuilder import *
import math


vOff=0.3
zRot=math.pi/2 # correct for vehicle axis being y-forward
zRot=0

# Append ATRV robot to the scene
segway = WheeledRobot('segwayrmp400')
segway.properties(Class="SegwayRMP400PhysicsClass", Path="morse/robots/segwayrmp400")
#segway.translate(z=vOff)
#segway.rotate(z=-3.0)
#segway.remove_wheels()

# Append an actuator
motion = Actuator('vw_diff_drive')
#motion.translate(z=vOff)
segway.append(motion)
motion.configure_mw('ros')
motion.configure_modifier('NED')


# Append an IMU sensor
imu = Sensor('imu')
imu.translate(z=vOff)
imu.rotate(x=math.pi,z=zRot)
segway.append(imu)
imu.configure_mw('ros')


# Append a Pose sensor
pose = Sensor('pose')
pose.translate(z=vOff)
pose.rotate(z=zRot)
segway.append(pose)
pose.configure_mw('ros')

# Append a Wheel Encoder sensor
#encoders = Sensor('wheel_encoders')
#encoders.translate(z=vOff)
#encoders.rotate(z=zRot)
#segway.append(encoders)

# Append a GPS sensor
gps = Sensor('gps')
gps.translate(z=vOff)
gps.rotate(z=zRot)
segway.append(gps)
gps.configure_mw('ros')

segway.translate(z=0.2)


# Configure the environment
env = Environment('is4s/large_field')
env.aim_camera([1.0470, 0, 0.7854])
