from setuptools import setup
import os #incluir
from glob import glob #incluir

package_name = 'ysolve_bot_subscriber'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')) #incluir
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
         'ysolve_bot_odom_subscriber = ysolve_bot_subscriber.ysolve_bot_odom_subscriber:main',
         'ysolve_bot_map_pos_subscriber = ysolve_bot_subscriber.ysolve_bot_map_pos_subscriber:main'
        ],
    },
)
