#!/usr/bin/env python
# encoding: utf-8

##
# BSD License
##
# Copyright (c) 2011, William Woodall (wjwwood@gmail.com)
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer. Redistributions in binary
# form must reproduce the above copyright notice, this list of conditions and
# the following disclaimer in the documentation and/or other materials
# provided with the distribution. Neither the name of the software nor the
# names of its contributors may be used to endorse or promote products derived
# from this software without specific prior written permission. 
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
##

"""
joy_to_twist.py - Provides Twist messages given a joy topic.

Parameters:
    linear_scalar (default: 1.0) This is a linear scalar that is multiplied by
    the joystick message. (2.0 will result in a 2.0 m/s cmd_vel with a
    joystick msg of 1.0)

    angular_scalar (default: 0.2) This is a linear scalar
    that is multiplied by the joystick message. (0.2 will result in a 0.2
    rad/s cmd_vel with a joystick msg of 1.0)

Topics:
    Subcribes to joy (sensor_msgs/Joy)
    Publishes to cmd_vel (geometry_msgs/Twist)

Created by William Woodall on 2010-07-12.
"""
__author__ = "William Woodall"

###  Imports  ###

# ROS imports
import roslib; roslib.load_manifest('segway_joy_teleop')
import rospy

# ROS msg and srv imports
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
from libsegwayrmp440.msg import Rmp440Command

# Python Libraries
import traceback

class SegwayJoyTeleop(object):
    """Joy2Twist ROS Node"""
    def __init__(self):
        # Initialize the Node
        rospy.init_node("SegwayJoyTeleop")
        
        # Get the linear scalar and angular scalar parameter
        self.LINEAR_SCALAR = rospy.get_param('~max_linear_vel', 0.2)
        self.ANGULAR_SCALAR = rospy.get_param('~max_angular_vel', 0.05)
        rospy.loginfo("Using max_linear_vel: %f and max_angular_vel: %f" %
                      (self.LINEAR_SCALAR, self.ANGULAR_SCALAR))
        
        # Setup the Joy topic subscription
        self.joy_subscriber = rospy.Subscriber("joy", Joy, self.handleJoyMessage, queue_size=1)
        
        # Setup the Twist topic publisher
        self.twist_publisher = rospy.Publisher("~cmd_vel", Twist, queue_size = 1)

        self.cmd_publisher = rospy.Publisher("~rmp_cmd", Rmp440Command, queue_size = 10)

        # Spin
        rospy.spin()

    def handleJoyMessage(self, data):
        """Handles incoming Joy messages"""
        msg = Twist()

        #see if a command has been requested by the joystick
        if data.buttons[8]==1 and data.buttons[9]==1:
            #send powerdown command
            rospy.loginfo("Shutting down.")
            cmd = Rmp440Command()
            cmd.command = 0
            cmd.parameter = 5
            self.cmd_publisher.publish(cmd)
        elif data.buttons[8]==1:
            rospy.loginfo("Set standby mode.")
            cmd = Rmp440Command()
            cmd.command = 0
            cmd.parameter = 3
            self.cmd_publisher.publish(cmd)
        elif data.buttons[9]==1:
            rospy.loginfo("Set tractor mode.")
            cmd = Rmp440Command()
            cmd.command = 0
            cmd.parameter = 4
            self.cmd_publisher.publish(cmd)
        elif data.buttons[0] == 1:
            rospy.loginfo("Play song 12.")
            cmd=Rmp440Command()
            cmd.command = 1
            cmd.parameter = 12
            self.cmd_publisher.publish(cmd)
        elif data.buttons[3] == 1:
            rospy.loginfo("Play song 13.")
            cmd=Rmp440Command()
            cmd.command = 1
            cmd.parameter = 13
            self.cmd_publisher.publish(cmd)

        # only send command if trigger is being held
        if (data.buttons[4]==1):
            trigger_val = data.axes[2]
            trigger_val += 1
            trigger_val /= 2
            trigger_val = 1 - trigger_val
            msg.linear.x = data.axes[1]
            scalar = (self.LINEAR_SCALAR/4.0 + trigger_val*(self.LINEAR_SCALAR*3.0/4.0))
            if (data.buttons[5]==1):
                scalar = scalar *2
            msg.linear.x *= scalar
            msg.angular.z = data.axes[0]
            scalar = (self.ANGULAR_SCALAR/4.0 + trigger_val*(self.ANGULAR_SCALAR*3.0/4.0))
            if (data.buttons[5]==1):
                scalar = scalar *2
            msg.angular.z *= scalar
            self.twist_publisher.publish(msg)
    

###  If Main  ###
if __name__ == '__main__':
    try:
        SegwayJoyTeleop()
    except:
        rospy.logerr("Unhandled Exception in the joy2Twist"+
                     " Node:+\n"+traceback.format_exc())
