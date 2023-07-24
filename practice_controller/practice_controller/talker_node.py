#!/usr/bin/env python3

import rclpy
from rclpy.node import Node


class talkerNode(Node) :
    def __init__() :
        super().__init__("talker_node")


def main(args = None) :
    rclpy.init(args = args) 



    rclpy.shutdown()