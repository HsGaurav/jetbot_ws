### Install ROS Melodic

http://wiki.ros.org/melodic/Installation/Ubuntu
(install cuda if not installed)

### Create catkin workspace

Create a ROS Catkin workspace to contain our ROS packages:

```bash
# create the catkin workspace
$ mkdir -p ~/workspace/jetbot_ws/src
Clone packages
$ git clone https://github.com/HsGaurav/jetbot_ws
# paste both the folders in ~/workspace/jetbot_ws/src
$ cd ~/workspace/jetbot_ws
$ catkin_make

# add jetbot_ws path to bashrc
$ sudo sh -c 'echo "source ~/workspace/jetbot_ws/devel/setup.bash" >> ~/.bashrc'

```
> Note:  out of personal preference, my jetbot_ws is created as a subdirectory under ~/workspace

Close and open a new terminal window.
Verify that your jetbot_ws is visible to ROS:
```bash
$ echo $ROS_PACKAGE_PATH 
/home/nvidia/workspace/jetbot_ws/src:/opt/ros/melodic/share
```

### Testing lane and obstacle environment

Testing environments

```bash
# For obstacle environment
$ roslaunch jetbot_gazebo obstacle_land.launch
# For lane environment
$ roslaunch jetbot_gazebo lane.launch
```
this will load the environment and let you test both lane and obstacle environment


### Controlling the bot

After you load the environment open a new terminal 

```bash
# install teleop_twist_keyboard
$ sudo apt-get install ros-melodic-teleop-twist-keyboard
# run teleop_twist_keyboard
$ rosrun teleop_twist_keyboard teleop_twist_keyboard.py

# After installing and running the teleop_twist_keyboard open a new terminal and run a python teleoperation file
$ chmod +x ~/workspace/jetbot_ws/src/jetbot_gazebo/launch/subcmdvel.py
$ roslaunch jetbot_gazebo subcmdvel.py
```

Now to control the jetbot with keyboard click on the terminal where you executed teleop-twist-keyboard
and use the following keys to control the bot
```bash
i : forward
j : left
l : right
, : reverse
k/(anykey) : stop
```
