#!/bin/bash
# 檢查是否安裝了 pygame
python3 -c "import pygame" &> /dev/null
if [ $? -ne 0 ]; then
    echo "正在安裝 pygame..."
    pip3 install pygame
fi

echo "正在啟動 Python 貪吃蛇遊戲..."
python3 snake_game.py
