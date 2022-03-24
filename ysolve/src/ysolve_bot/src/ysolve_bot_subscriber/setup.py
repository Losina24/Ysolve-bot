from setuptools import setup
import os 
from glob import glob

package_name = 'ysolve_bot_subscriber'

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
    maintainer='alosa',
    maintainer_email='alosa@idealista.com',
    description='Paquete de subscripción del bot Ysolve',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            	'odom_pos_subscriber = ysolve_bot_position_subscriber.odom_pos_subscriber:main',
            	'map_pos_subscriber = ysolve_bot_position_subscriber.map_pos_subscriber:main',
        ],
    },
)
