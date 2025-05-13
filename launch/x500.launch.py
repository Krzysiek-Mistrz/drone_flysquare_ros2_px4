import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess, IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    # Gazebo
    px4_sitl = ExecuteProcess(
        cmd=['make', 'px4_sitl', 'gz_x500'],
        cwd=os.path.expanduser('~/PX4-Autopilot'),
        output='screen'
    )

    # Micro-ROS-agent
    micro_ros_agent = ExecuteProcess(
        cmd=['MicroXRCEAgent', 'udp4', '-p', '8888'],
        output='screen'
    )

    # Our Node
    square_flight = Node(
        package='drone_fly_square',
        executable='drone_fly_square',
        name='drone_fly_square',
        output='screen'
    )

    return LaunchDescription([
        px4_sitl,
        micro_ros_agent,
        square_flight,
    ])
