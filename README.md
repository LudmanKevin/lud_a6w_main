# lud_a6w_main
ROS 2 python package.  [![Static Badge](https://img.shields.io/badge/ROS_2-Humble-34aec5)](https://docs.ros.org/en/humble/)

### Működés leírása
A traffic_light_monitor egy jelzőlámpa és egy jármű viszonyát hivatott szimulálni. A jelzőlámpa szerepét a traffic_light_publiser látja el. Három féle állapot között válakozik: piros, sárga és zöld. A jármű szerepét a vehicle_monitor_node látja el, és a traffic_light_publiser által hirdetett lámpaállapotokra reagál: ha piros, akkor megáll, ha sárga akkor lassít, és ha zöld, akkor elindul.

### Clone the packages
``` r
cd ~/ros2_ws/src
```
``` r
git clone https://github.com/LudmanKevin/lud_a6w_main
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