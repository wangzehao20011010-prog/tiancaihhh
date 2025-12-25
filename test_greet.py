#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test cases for the international greeting module
"""

import greet


def test_default_greeting():
    """Test default Chinese greeting"""
    result = greet.greet()
    assert result == "你好!", f"Expected '你好!', got '{result}'"
    print("✓ Default greeting test passed")


def test_chinese_greeting():
    """Test Chinese greeting explicitly"""
    result = greet.greet('zh')
    assert result == "你好!", f"Expected '你好!', got '{result}'"
    print("✓ Chinese greeting test passed")


def test_english_greeting():
    """Test English greeting"""
    result = greet.greet('en')
    assert result == "Hello!", f"Expected 'Hello!', got '{result}'"
    print("✓ English greeting test passed")


def test_greeting_with_name():
    """Test greeting with a name"""
    result = greet.greet('zh', '世界')
    assert result == "你好, 世界!", f"Expected '你好, 世界!', got '{result}'"
    print("✓ Greeting with name test passed")


def test_greeting_with_english_name():
    """Test English greeting with a name"""
    result = greet.greet('en', 'World')
    assert result == "Hello, World!", f"Expected 'Hello, World!', got '{result}'"
    print("✓ English greeting with name test passed")


def test_invalid_language():
    """Test fallback to Chinese for invalid language code"""
    result = greet.greet('invalid')
    assert result == "你好!", f"Expected '你好!' (fallback), got '{result}'"
    print("✓ Invalid language fallback test passed")


def test_list_languages():
    """Test listing all available languages"""
    languages = greet.list_languages()
    assert 'zh' in languages, "Chinese should be in languages"
    assert 'en' in languages, "English should be in languages"
    assert languages['zh'] == '你好', "Chinese greeting should be '你好'"
    assert len(languages) >= 10, "Should have at least 10 languages"
    print("✓ List languages test passed")


if __name__ == '__main__':
    test_default_greeting()
    test_chinese_greeting()
    test_english_greeting()
    test_greeting_with_name()
    test_greeting_with_english_name()
    test_invalid_language()
    test_list_languages()
    print("\n✅ All tests passed!")
