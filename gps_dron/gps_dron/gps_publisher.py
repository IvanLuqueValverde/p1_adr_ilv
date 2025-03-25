import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix
import random

class GPSPublisher(Node):
    def __init__(self):
        super().__init__('gps_publisher')
        self.publisher_ = self.create_publisher(NavSatFix, '/gps_position', 10)
        self.timer = self.create_timer(1.0, self.publish_gps_data)
        self.get_logger().info('GPS Publisher Node has started.')

    def publish_gps_data(self):
        msg = NavSatFix()
        msg.latitude = random.uniform(-90.0, 90.0)  # Simulación de latitud
        msg.longitude = random.uniform(-180.0, 180.0)  # Simulación de longitud
        msg.altitude = random.uniform(0.0, 1000.0)  # Simulación de altitud

        self.publisher_.publish(msg)
        self.get_logger().info(f'Published GPS Data: {msg.latitude}, {msg.longitude}, {msg.altitude}')

rclpy.init()
node = GPSPublisher()
rclpy.spin(node)
