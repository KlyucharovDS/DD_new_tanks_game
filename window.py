#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame

from variables import *
from colors import *


class Window:

    def __init__(self, window_title: str, icon=None) -> None:
        """
        Инициализация и отрисовка окна
        :param window_title: название окна
        :return:
        """
        pygame.init()
        self.__window = pygame.display.set_mode((HEIGTH,WIDTH), pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.RESIZABLE)
        pygame.display.set_caption(window_title)
        pygame.display.set_icon(pygame.image.load('images/logo.png'))

    def show_menu(self) -> int:
        """
        Отображение меню и обработка нажатия клавишь
        :return: количество игроков
        """
        count_players = 1
        # -------------players----------------
        y = {1:WIDTH/2+100,2:WIDTH/2+150}
        x_text = HEIGTH/2-50
        text_size=30
        self.write_text('1 player', (x_text,y[1]), text_size)
        self.write_text('2 players', (x_text,y[2]), text_size)
        # рисование треугольника у "player 1"
        coord_triangle = {1:((x_text-50,y[1]+text_size/2-10), ((x_text-50,y[1]+text_size/2+10)),((x_text-20,y[1]+text_size/2))),
                          2:(((x_text-50,y[2]+text_size/2-10), ((x_text-50,y[2]+text_size/2+10)),((x_text-20,y[2]+text_size/2))))}
        self.paint_triangle(YELLOWGREEN, coord_triangle[1])
        clock = pygame.time.Clock()
        show = True
        while show:
            # ----------events---------------
            for event in pygame.event.get():
                # exit
                if event.type == pygame.QUIT:
                    show = False
                if event.type ==pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                        self.paint_triangle(BLACK, coord_triangle[count_players])
                        count_players = 2 if count_players==1 else 1
                        self.paint_triangle(YELLOWGREEN, coord_triangle[count_players])

                    if event.key == pygame.K_KP_ENTER or \
                    event.key == pygame.K_RETURN or \
                    event.key ==pygame.K_SPACE:
                        print(f'pressing enter, count players: {count_players}')
                        show=False
                    # exit
                    if event.key == pygame.K_ESCAPE:
                        break
                if event.type == pygame.KEYUP:
                    # exit
                    if event.key == pygame.K_ESCAPE:
                        break
            # update and delay
            clock.tick(FPS)
            pygame.display.update()
        # handling choose gamer after press 'Enter' button
        else:
            # @todo create entities Player
            pass
        pygame.quit()
        return count_players

    def write_text(self, text: str,
                   coord: tuple,
                   size: int,
                   color=WHITE,
                   font='arial'
                   ):
        """
        Напечататеть текст на текущем окне
        :param text: печатаемый текст
        :param coord: координаты в формате кортежа (x,y)
        :param size: размер печатаемого текста
        :param color: цвет в формате кортежа (R,G,B)
        :return: None
        """
        f = pygame.font.SysFont(font, size)
        txt = f.render(text, True, color,BLACK)
        pos = txt.get_rect(center=coord)
        self.__window.blit(txt, coord)

    def paint_triangle(self, color:tuple, coord)->None:
        """
        Нарисовать закрашенный треугольник
        :param color: цвета из модуля color
        :param coord: координаты вершин в формате кортежа (x,y)
        :return:
        """
        pygame.draw.polygon(self.__window, color,coord)

# # @todo pattern на будущее
# keys = pygame.key.get_pressed()
# if keys[self.keyLEFT]:
#     pass
# elif keys[self.keyRIGHT]:
#     pass
# elif keys[self.keyUP]:
#     pass
# elif keys[self.keyDOWN]:
#     pass