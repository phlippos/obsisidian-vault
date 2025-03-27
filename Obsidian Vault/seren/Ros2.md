## Remapping:
- ros2 run turtlesim turtle_teleop_key --ros-args --remap turtle1/cmd_vel:=turtle2/cmd_vel
-  if you try to run the same command as before, you will notice that this one also controls `turtle1`. The way to change this behavior is by remapping the `cmd_vel` topic.
- [Remapping](https://design.ros2.org/articles/ros_command_line_arguments.html#name-remapping-rules) allows you to reassign default node properties, like node name, topic names, service names, etc., to custom values
## Ros Nodes
Each node in ROS should be responsible for a single, modular purpose, e.g. controlling the wheel motors or publishing the sensor data from a laser range-finder. Each node can send and receive data from other nodes via topics, services, actions, or parameters.

## ros2 node list
- `ros2 node list` will show you the names of all running nodes.
## ros2 node info
- ros2 node info <node_name>
- Now that you know the names of your nodes, you can access more information about them with
- `ros2 node info` returns a list of subscribers, publishers, services, and actions. i.e. the ROS graph connections that interact with that node. 

## Topics
- ROS 2 breaks complex systems down into many modular nodes. Topics are a vital element of the ROS graph that act as a bus for nodes to exchange messages.
- ![[Pasted image 20240516173608.png]]
- A node may publish data to any number of topics and simultaneously have subscriptions to any number of topics.
- Topics are one of the main ways in which data is moved between nodes and therefore between different parts of the system.
- Running the `ros2 topic list` command in a new terminal will return a list of all the topics currently active in the system
- `ros2 topic list -t` will return the same list of topics, this time with the topic type appended in brackets
- to see the data being published on a topic, use: ros2 topic echo <topic_name>
- Topics don’t have to only be one-to-one communication; they can be one-to-many, many-to-one, or many-to-many.
- ros2 topic info /turtle1/cmd_vel
- Nodes send data over topics using messages. Publishers and subscribers must send and receive the same type of message to communicate.
- Now we can run `ros2 interface show <msg type>` on this type to learn its details.
- ros2 topic pub: Now that you have the message structure, you can publish data to a topic directly from the command line using:
- ros2 topic pub <topic_name><msg_type> '<**args**>'
- The `'<args>'` argument is the actual data you’ll pass to the topic, in the structure
- ros2 topic pub --once /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"
- `--once` is an optional argument meaning “publish one message then exit”
- The turtle require a steady stream of commands to operate continuously. So, to get the turtle to keep moving, you can run:
- ros2 topic pub --rate 1 /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"
- The difference here is the removal of the `--once` option and the addition of the `--rate 1` option, which tells `ros2 topic pub` to publish the command in a steady stream at 1 Hz.
-  you can view the rate at which data is published using: ros2 topic hz /turtle1/pose

## Services
- Services are another method of communication for nodes in the ROS graph. Services are based on a call-and-response model versus the publisher-subscriber model of topics. While topics allow nodes to subscribe to data streams and get continual updates, <mark style="background: #FFB86CA6;">services only provide data when they are specifically called by a client.</mark>
- Running the `ros2 service list` command in a new terminal will return a list of all the services currently active in the system
#### ros2 service type <service_name>
- To find out the type of a service, use the command
- To see the types of all the active services at the same time, you can append the `--show-types` option, abbreviated as `-t`, to the `list` command: ros2 service list -t
#### ros2 service find
- If you want to find all the services of a specific type, you can use the command: ros2 service find <type_name>
#### ros2 interface show
- You can call services from the command line, but first you need to know the structure of the input arguments.
- ros2 interface show <type_name>
#### ros2 service call
- Now that you know what a service type is, how to find a service’s type, and how to find the structure of that type’s arguments, you can call a service using
- ros2 service call <service_name> <service_type> <**arguments**>
- The `<arguments>` part is optional. For example, you know that `Empty` typed services don’t have any arguments
- ros2 service call /spawn turtlesim/srv/Spawn "{x: 2, y: 2, theta: 0.2, name: ''}"

## Parameters
- A parameter is a configuration value of a node. You can think of parameters as node settings. A node can store parameters as integers, floats, booleans, strings, and lists. In ROS 2, each node maintains its own parameters.
#### ros2 param list
- To see the parameters belonging to your nodes, open a new terminal and enter the command
- ros2 param list
#### ros2 param get
- to display the type and current value of a parameter, use  the command:
- ros2 param get <node_name> <parameter_name>
#### ros2 param set
- To change a parameter’s value at runtime
- ros2 param set <node_name> <parameter_name> <**value**>
#### ros2 param dump
- You can view all of a node’s current parameter values by using the command : ros2 param dump <node_name>
#### ros2 param load
- You can load parameters from a file to a currently running node using the command: ros2 param load <node_name> <parameter_file>
#### load parameter file on node startup
- To start the same node using your saved parameter values, use: ros2 run <package_name> <executable_name> --ros-args --params-file <file_name>
#### Actions
- Actions are one of the communication types in ROS 2 and are intended for long running tasks. They consist of three parts: a goal, feedback, and a result.
- Actions are built on topics and services. Their functionality is similar to services, except actions can be canceled. They also provide steady feedback, as opposed to services which return a single response.
- Actions use a client-server model, similar to the publisher-subscriber model
- An “action client” node sends a goal to an “action server” node that acknowledges the goal and returns a stream of feedback and a result.
- ![[Pasted image 20240516181112.png]]
- Each time you press one of these keys, you are sending a goal to an action server that is part of the `/turtlesim` node. The goal is to rotate the turtle to face a particular direction.
#### ros2 action list
- To identify all the actions in the ROS graph, run the command:
- ros2 action list
- Actions have types, similar to topics and services.
- ros2 action list -t
#### ros2 action info 
- ros2 action info /turtle1/rotate_absolute

#### ros2 interface show
- action goal yourself is the structure of the action type
- ros2 interface show turtlesim/action/RotateAbsolute
#### ros2 action send_goal
- Now let’s send an action goal from the command line with the following syntax: ros2 action send_goal <action_name> <action_type> <**values**>
- ros2 action send_goal /turtle1/rotate_absolute turtlesim/action/RotateAbsolute "{theta: 1.57}"
- o see the feedback of this goal, add `--feedback` to the `ros2 action send_goal` command:
- ros2 action send_goal /turtle1/rotate_absolute turtlesim/action/RotateAbsolute "{theta: -1.57}" --feedback

### launching nodes
- you create more complex systems with more and more nodes running simultaneously, opening terminals and reentering configuration details becomes tedious.
- Launch files allow you to start up and configure a number of executables containing ROS 2 nodes simultaneously.
- Running a single launch file with the `ros2 launch` command will start up your entire system - all nodes and their configurations - at once.
```python
 # turtlesim/launch/multisim.launch.py

from launch import LaunchDescription
import launch_ros.actions

def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(
            namespace= "turtlesim1", package='turtlesim', executable='turtlesim_node', output='screen'),
        launch_ros.actions.Node(
            namespace= "turtlesim2", package='turtlesim', executable='turtlesim_node', output='screen'),
    ])
```
