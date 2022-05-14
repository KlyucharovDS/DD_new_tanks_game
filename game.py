#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Модуль управления последовательностью игры:
    * отображение меню
    * выбор количества игроков
    * подсчёт очков игроков
    ....
"""
from variables import *
import player
from pygame.locals import *
import pygame



PLAYER1= None
PLAYER2= None

def init_game(window):
    f=pygame.font.SysFont('arial', 30)
    text=f.render('test TEXT',True,WHITE,BLACK)
    pos = text.get_rect(center=(WIDTH/2,HEIGTH/2))
    window.blit(text,pos)

def set_text():
    pass



