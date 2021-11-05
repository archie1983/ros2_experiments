import os
from glob import glob
from setuptools import setup
from setuptools import find_packages

package_name = 'walking_robot_tutorial_urdf'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.py')),
        (os.path.join('share', package_name), glob('urdf/*')),
#        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.launch.py'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Arturs Elksnis',
    maintainer_email='arturs@elksnis.co.uk',
    description='Walking robot demo',
    license='Apache 2.0 License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'walker_state_publisher = walking_robot_tutorial_urdf.walker_state_publisher:main',
        ],
    },
)
