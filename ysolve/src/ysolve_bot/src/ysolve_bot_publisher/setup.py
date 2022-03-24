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
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Raul',
    maintainer_email='raul@rdelaf.upv.es',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
       	'position1_publisher = ysolve_bot_publisher.position1_publisher:main',
        	'position2_publisher = ysolve_bot_publisher.position2_publisher:main',
        	'position3_publisher = ysolve_bot_publisher.position3_publisher:main',
        ],
    },
)
