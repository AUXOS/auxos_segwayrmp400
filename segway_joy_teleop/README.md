# Joy To Twist

Subscribes to a sensor_msgs/Joy and publishes a geometry_msgs/Twist message.  The joystick commands are scaled using the "max_linear_vel" and "max_angular_vel" parameters.  Pressing button 5 (top right trigger) on the joystick doubles the maximum values.  Button 4 (top left trigger) serves as a deadman switch and must be held for commands to be published.
