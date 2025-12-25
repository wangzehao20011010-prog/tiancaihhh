#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Simple greeting module responding to 你好 (Hello)
"""

def greet(name="朋友"):
    """
    Return a greeting message in Chinese
    
    Args:
        name: Name of the person to greet (default: "朋友" which means "friend")
    
    Returns:
        A greeting string
    """
    return f"你好，{name}！"


if __name__ == "__main__":
    print(greet())
