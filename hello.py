#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的问候程序
A simple greeting application
"""


def greet(name=None):
    """
    返回问候语
    Return a greeting message
    
    Args:
        name (str, optional): 要问候的名字 / Name to greet
        
    Returns:
        str: 问候消息 / Greeting message
    """
    if name:
        return f"你好, {name}!"
    return "你好!"


def main():
    """主函数 / Main function"""
    print(greet())
    print(greet("世界"))  # Hello, World!


if __name__ == "__main__":
    main()
