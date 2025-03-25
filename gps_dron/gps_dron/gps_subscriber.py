import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix

class GPSSubscriber(Node):
    def __init__(self):
        super().__init__('gps_subscriber')
        self.subscription = self.create_subscription(
            NavSatFix,
            '/gps_position',
            self.gps_callback,
            10)
        self.get_logger().info('GPS Subscriber Node has started.')

    def gps_callback(self, msg):
        self.get_logger().info(f'Received GPS Data: {msg.latitude}, {msg.longitude}, {msg.altitude}')

rclpy.init()
node = GPSSubscriber()
rclpy.spin(node)