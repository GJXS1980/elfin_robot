#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy, sys
import moveit_commander

class MoveItFkDemo:
    def __init__(self):
        # 初始化move_group的API
        moveit_commander.roscpp_initialize(sys.argv)

        # 初始化ROS节点
        rospy.init_node('moveit_fk_demo', anonymous=True)
 
        # 初始化需要使用move group控制的机械臂中的arm group
        #arm = moveit_commander.MoveGroupCommander('manipulator')
        arm = moveit_commander.MoveGroupCommander('elfin_arm')
        
        # 设置机械臂运动的允许误差值
        arm.set_goal_joint_tolerance(0.001)

        # 设置允许的最大速度和加速度
        arm.set_max_acceleration_scaling_factor(0.5)
        arm.set_max_velocity_scaling_factor(0.5)
        
        # 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        #joint_positions = [2.439924955368042, -1.248072926198141, 0.9999423027038574, -1.254838768635885, -1.573728386555807, -0.15925771394838506]
        joint_positions = [0.8992990846345683, 1.0661095282389927, 1.401540626687011, -0.001309009595602908, -0.3411863741392006, -1.093061456772679]

        arm.set_joint_value_target(joint_positions)

        # 控制机械臂完成运动
        arm.go()
        rospy.sleep(1)
        
        # 关闭并退出moveit
        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)

if __name__ == "__main__":
    try:
        MoveItFkDemo()
    except rospy.ROSInterruptException:
        pass