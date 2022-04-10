from setuptools import setup
import os
from glob import glob 

package_name = 'ysolve_bot_publisher'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')) # incluir
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
        	'ysolve_bot_publisher = ysolve_bot_publisher.ysolve_bot_publisher:main',
        	'initial_pose = ysolve_bot_publisher.initial_pose:main',
        	'go_to_pos = ysolve_bot_publisher.go_to_pos:main'
        ],
    },
)
