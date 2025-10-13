from setuptools import setup

package_name = 'traffic_light_monitor'

setup(
    name=package_name,
    version='1.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ludmán Kevin',
    maintainer_email='ludmankevin@gmail.com',
    description='Jármű reakciói egy közlekedési lámpa lehetséges állapotaira.',
    license='MIT',
    entry_points={
        'console_scripts': [
            'traffic_light_publisher = traffic_light_monitor.traffic_light_publisher:main',
            'vehicle_monitor_node = traffic_light_monitor.vehicle_monitor_node:main',
        ],
    },
)