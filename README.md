### Install ROS Melodic

http://wiki.ros.org/melodic/Installation/Ubuntu
(install cuda if not installed)

### Make package

Extract the workspace and follow instructions

```bash
# move to the workspace
$ cd jetbot_ws
$ catkin_make

Whenever you open a new terminal ensure that you source the package
$ source {path to jetbot_ws}/jetbot_ws/devel/setup.bash
```

### Testing lane and obstacle environment

Before Testing environments extract `model_editor_models.zip` and copy the `unit_box_wall` `wallx` `wally` into  `~/.gazebo`

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
