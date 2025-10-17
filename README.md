# lud_a6w_main
ROS 2 python package.  [![Static Badge](https://img.shields.io/badge/ROS_2-Humble-34aec5)](https://docs.ros.org/en/humble/)

### Clone the packages
``` r
cd ~/ros2_ws/src
```
``` r
git clone https://github.com/sze-info/ros2_py_template
```


### Build ROS 2 packages
``` r
colcon build --packages-select traffic_light_monitor
```
``` r
source install/setup.bash
```
``` r
ros2 launch traffic_light_monitor traffic_light_system.launch.py
```