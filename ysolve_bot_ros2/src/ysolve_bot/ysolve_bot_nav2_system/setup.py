import os
from glob import glob
from setuptools import setup

package_name = 'ysolve_bot_nav2_system'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'config'), glob('config/*.pgm')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
        (os.path.join('share', package_name, 'rviz'), glob('rviz/*.rviz')),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),  
        (os.path.join('share', package_name, 'config'), glob('config/*.lua')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')), 
        (os.path.join('share', package_name, 'config'), glob('config/*.xml')) 
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yeray',
    maintainer_email='ycansam@epsg.upv.es',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'nav_to_pose = ysolve_bot_nav2_system.nav_to_pose:main',
        	'nav_to_waypoints = ysolve_bot_nav2_system.nav_to_waypoints:main',
        ],
    },
)
