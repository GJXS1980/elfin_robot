#   启动pc与机械臂通信
```bash
#   启动elfin_robot_bringup
roslaunch elfin_robot_bringup elfin5_test.launch

#   启动机器人控制
sudo chrt 10 bash
roslaunch elfin_robot_bringup elfin_ros_control_v2.launch
```

#   控制机械臂
### 关节角度
```bash
#   查询关节角度，position为六个关节角度
rostopic echo /joint_states
```
在ur_planning/scripts/joint_planning.py文件下，把相应的六个关节角度替换掉，就可以控制机器人到达相应的位姿
```bash
rosrun elfin_planning joint_planning.py
```

### 位姿
```bash
#   获取当前机械臂的位姿，Translation为位置，Quaternion为四元数
rosrun tf tf_echo base_link ee_link
```
在/elfin_planning/scripts/pose_planning.py文件下，把相应的位置和四元数替换，就可以控制机器人到达相应的位姿
```bash
rosrun elfin_planning pose_planning.py
```