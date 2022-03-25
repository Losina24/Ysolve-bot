from setuptools import setup

package_name = 'ysolve_nav2_system'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
        (os.path.join('share', package_name, 'config'), glob('config/*.pgm')),
        (os.path.join('share', package_name, 'config'), glob('config/*.rviz')),
        (os.path.join('share', package_name, 'config'), glob('config/*.xml'))
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
            # Scripts to run in this package
            'initial_pose_pub = ysolve_nav2_system.initial_pose_pub:main',
            'load_map = ysolve_nav2_system.load_map:main',
            'nav_to_pose = ysolve_nav2_system.nav_to_pose:main',
            'go_to_pose = ysolve_nav2_system.go_to_pose:main'
        ],
    },
)
