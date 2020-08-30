### Install ROS Melodic

```bash
# enable all Ubuntu packages:
$ sudo apt-add-repository universe
$ sudo apt-add-repository multiverse
$ sudo apt-add-repository restricted

# add ROS repository to apt sources
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
$ sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

# install ROS Base
$ sudo apt-get update
$ sudo apt-get install ros-melodic-ros-base

# add ROS paths to environment
sudo sh -c 'echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc'
```

Close and restart the terminal.

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

First open a new terminal, and start `roscore`
```bash
$ roscore
```

1. Obstacle environment

```bash
$ nano ~/workspace/jetbot_ws/src/jetbot_gazebo/launch/main.launch
```
Edit the world to `obstacle_land.world`

2. Lane environment

Edit the world to `lane.world`

```bash
$ roslaunch jetbot_gazebo main.launch
```
this will load the environment and let you test both lane and obstacle environment


### Controlling the bot

After you load the environment open a new terminal 

```bash
# install teleop_twist_keyboard
$ sudo apt-get install ros-noetic-teleop-twist-keyboard
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
