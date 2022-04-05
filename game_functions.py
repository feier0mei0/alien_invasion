
import sys
import pygame


def check_event():
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event == pygame.QUIT:
            sys.exit()


