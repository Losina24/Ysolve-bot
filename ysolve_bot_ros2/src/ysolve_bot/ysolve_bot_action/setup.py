from setuptools import setup
import os
from glob import glob

package_name = 'ysolve_bot_action'

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
    maintainer='yeray',
    maintainer_email='ycansam@epsg.upv.es',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'action_server = ysolve_bot_action.action_server:main',
            'action_client = ysolve_bot_action.action_client:main'
        ],
    },
)
