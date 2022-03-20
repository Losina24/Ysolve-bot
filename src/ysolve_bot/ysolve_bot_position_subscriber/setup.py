from setuptools import setup
import os 
from glob import glob

package_name = 'robot_position_subscriber'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='danielBurruchaga',
    maintainer_email='dbursol@upv.epsg.es',
    description='Nav module for ROs2',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'odom_pos_subscriber = robot_position_subscriber.odom_pos_subscriber:main',
            'map_pos_subscriber = robot_position_subscriber.map_pos_subscriber:main',

        ],
    },
)
