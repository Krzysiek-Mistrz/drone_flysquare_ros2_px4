from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'drone_fly_square'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='developer',
    maintainer_email='krzyskuar@gmail.com',
    description='flying on square',
    license='GNU GPL V3',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'drone_fly_square = drone_fly_square.drone_fly_square:main',
        ],
    },
)