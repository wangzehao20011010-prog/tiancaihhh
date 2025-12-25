#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
International Greeting Module
Provides greetings in multiple languages
"""

GREETINGS = {
    'zh': '你好',      # Chinese - nihao
    'en': 'Hello',     # English
    'es': 'Hola',      # Spanish
    'fr': 'Bonjour',   # French
    'de': 'Guten Tag', # German
    'ja': 'こんにちは', # Japanese
    'ko': '안녕하세요',  # Korean
    'ar': 'مرحبا',     # Arabic
    'ru': 'Здравствуйте', # Russian
    'pt': 'Olá',       # Portuguese
}


def greet(language='zh', name=None):
    """
    Greet in the specified language
    
    Args:
        language (str): Language code (default: 'zh' for Chinese)
        name (str): Optional name to greet
        
    Returns:
        str: Greeting message
    """
    greeting = GREETINGS.get(language, GREETINGS['zh'])
    
    if name:
        return f"{greeting}, {name}!"
    return f"{greeting}!"


def list_languages():
    """
    List all available languages
    
    Returns:
        dict: Dictionary of language codes and greetings
    """
    return GREETINGS.copy()


if __name__ == '__main__':
    import sys
    
    # Default to Chinese greeting (nihao)
    if len(sys.argv) == 1:
        print(greet('zh'))
    elif len(sys.argv) == 2:
        # Language code provided
        lang = sys.argv[1]
        if lang == '--list':
            print("Available languages:")
            for code, greeting in sorted(GREETINGS.items()):
                print(f"  {code}: {greeting}")
        else:
            print(greet(lang))
    else:
        # Language code and name provided
        lang = sys.argv[1]
        name = ' '.join(sys.argv[2:])
        print(greet(lang, name))
