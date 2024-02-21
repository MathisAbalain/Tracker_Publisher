#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from tracker_publisher.vive_pb2 import GlobalMsg
import socket
from tracker_publisher.vive_utils import *
from geometry_msgs.msg import TransformStamped

import tf2_ros
from tf2_ros import TransformBroadcaster


class ViveReceiverNode(Node): 
    def __init__(self):
        super().__init__('vive_receiver_node')

        # Creation de la socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(("", VIVE_SERVER_PORT))

        self.get_logger().info("test")

        # Creation du publisher
        # self.publisher = self.create_publisher(String, 'vive_messages', 10)
        self.publisher = self.create_publisher(TransformStamped, 'tf_topic', 10)

        self.tf_broadcaster = TransformBroadcaster(self)


        self.listen_for_messages()

    def listen_for_messages(self):
        while rclpy.ok():
            try:
                data, _ = self.server_socket.recvfrom(4069)
                self.get_logger().info("a l'ecoute")
                # Publication du message
                # pb_msg = GlobalMsg()
                # pb_msg.ParseFromString(data)


                trackerInfos = GlobalMsg_to_tracker_infos(data)
                tf_msgs = tracker_infos_to_tf(trackerInfos)
                self.get_logger().info("donnees tf")
                
                for tf_msg in tf_msgs:
                    print(tf_msg)
                    self.tf_broadcaster.sendTransform(tf_msg)

                # self.tf_broadcaster.sendTransform(tf_msgs[0])

                # self.publisher.publish(tf_msgs[0])

            except socket.error as e:
                self.get_logger().error(f"Error receiving Vive message: {str(e)}")



def main(args=None):
    rclpy.init(args=args)
    node = ViveReceiverNode()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()