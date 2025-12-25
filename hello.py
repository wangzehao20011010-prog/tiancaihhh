#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的问候程序
A simple greeting program
"""

WELCOME_MESSAGE = "欢迎来到源代码的小窝！"


def greet(name="朋友"):
    """
    问候函数
    Greeting function
    
    参数:
        name: 被问候者的名字，默认为"朋友"
    
    返回:
        问候语字符串
    """
    return f"你好，{name}！{WELCOME_MESSAGE}"


def main():
    """主函数"""
    print(greet())
    print(greet("天才"))
    print(greet("世界"))


if __name__ == "__main__":
    main()
