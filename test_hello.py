#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试问候程序
Tests for the greeting application
"""

import unittest
from hello import greet


class TestGreeting(unittest.TestCase):
    """测试问候功能 / Test greeting functionality"""
    
    def test_greet_without_name(self):
        """测试无名字的问候 / Test greeting without name"""
        result = greet()
        self.assertEqual(result, "你好!")
    
    def test_greet_with_name(self):
        """测试带名字的问候 / Test greeting with name"""
        result = greet("世界")
        self.assertEqual(result, "你好, 世界!")
    
    def test_greet_with_custom_name(self):
        """测试自定义名字的问候 / Test greeting with custom name"""
        result = greet("张三")
        self.assertEqual(result, "你好, 张三!")


if __name__ == "__main__":
    unittest.main()
