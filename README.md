# tiancaihhh
这是源代码的小窝

## International Greeting 国际问候

A simple greeting module that supports multiple languages.

### Usage 使用方法

```bash
# Default greeting in Chinese (你好)
python3 greet.py

# Greet in a specific language
python3 greet.py en        # Hello!
python3 greet.py zh        # 你好!
python3 greet.py es        # Hola!

# Greet with a name
python3 greet.py zh 世界    # 你好, 世界!
python3 greet.py en World  # Hello, World!

# List all available languages
python3 greet.py --list
```

### Supported Languages 支持的语言

- Chinese (zh): 你好
- English (en): Hello
- Spanish (es): Hola
- French (fr): Bonjour
- German (de): Guten Tag
- Japanese (ja): こんにちは
- Korean (ko): 안녕하세요
- Arabic (ar): مرحبا
- Russian (ru): Здравствуйте
- Portuguese (pt): Olá
