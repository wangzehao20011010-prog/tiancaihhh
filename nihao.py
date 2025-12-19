#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的中文问候程序
Simple Chinese greeting program
"""


def greet():
    """
    向用户打招呼
    Greet the user
    """
    return "你好"


def main():
    """
    主函数
    Main function
    """
    message = greet()
    print(message)


if __name__ == "__main__":
    main()
