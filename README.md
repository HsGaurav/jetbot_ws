### Install ROS Melodic

http://wiki.ros.org/melodic/Installation/Ubuntu
(install cuda if not installed)

### Install gazebo

```bash
# install default stable gazebo version
$ sudo apt install gazebo9
# install ros control package
$ sudo apt install ros-melodic-gazebo-ros-control ros-melodic-controller-manager ros-melodic-joint-trajectory-controller ros-melodic-ros-control ros-melodic-ros-controllers
```


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

Before Testing environments and move the folders `unit_box_wall` `wallx` `wally` from `model_editor_models` into  `~/.gazebo` directory

```bash
# For obstacle environment
$ roslaunch jetbot_gazebo obstacle.launch
# For lane environment
$ roslaunch jetbot_gazebo lane.launch
# For empty environment (only jetbot)
$ roslaunch jetbot_gazebo gazebo.launch
```
this will load the environment and let you test both lane and obstacle environment


### Controlling the bot

After you load the environment open a new terminal 

```bash
# install teleop_twist_keyboard
$ sudo apt-get install ros-melodic-teleop-twist-keyboard
# run teleop_twist_keyboard
$ rosrun teleop_twist_keyboard teleop_twist_keyboard.py

```

Now to control the jetbot use the following controls on the terminal where you executed teleop-twist-keyboard
```bash
#---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .

q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%
anything else : stop
```
