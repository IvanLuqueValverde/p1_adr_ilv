from setuptools import find_packages, setup

package_name = 'gps_dron'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='student',
    maintainer_email='ivanxd304@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'gps_publisher = gps_dron.gps_publisher:main',
        'gps_subscriber = gps_dron.gps_subscriber:main',
        ],
    },
)
