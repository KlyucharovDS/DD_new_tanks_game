# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from time import sleep

from GameSequence.game_mechanics import GameMechanics, GAME_MECHANICS
from GameSequence.tanks import BaseTank
from GameSequence.tank_field import Map
from colors import *
from variables import FPS, HEIGTH, WIDTH


class Window:

    def __init__(self, window_title: str, icon=None) -> None:
        """
        Инициализация и отрисовка окна
        :param window_title: название окна
        :return:
        """
        pygame.init()
        self.__window = pygame.display.set_mode((HEIGTH, WIDTH),
                                                pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.RESIZABLE)
        pygame.display.set_caption(window_title)
        pygame.display.set_icon(pygame.image.load(icon))

    def show_start_window(self):
        """
        Метод отображающий экран заставки перед показом меню
        @todo например выплывающая картинка с наименованием игры
        :return:
        """
        pass

    def show_menu(self) -> int:
        """
        Отображение меню и обработка нажатия клавишь
        :return: количество игроков
        """
        count_players = 1
        # -------------players----------------
        y = {1: WIDTH / 2 + 100, 2: WIDTH / 2 + 150}
        x_text = HEIGTH / 2 - 50
        text_size = 30
        self.write_text('1 player', (x_text, y[1]), text_size)
        self.write_text('2 players', (x_text, y[2]), text_size)
        # рисование треугольника у "player 1"
        coord_triangle = {1: ((x_text - 50, y[1] + text_size / 2 - 10), ((x_text - 50, y[1] + text_size / 2 + 10)),
                              ((x_text - 20, y[1] + text_size / 2))),
                          2: (((x_text - 50, y[2] + text_size / 2 - 10), ((x_text - 50, y[2] + text_size / 2 + 10)),
                               ((x_text - 20, y[2] + text_size / 2))))}
        self.paint_triangle(YELLOWGREEN, coord_triangle[1])
        clock = pygame.time.Clock()
        show = True
        while show:
            # ----------events---------------
            for event in pygame.event.get():
                # exit
                if event.type == pygame.QUIT:
                    show = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                        self.paint_triangle(BLACK, coord_triangle[count_players])
                        count_players = 2 if count_players == 1 else 1
                        self.paint_triangle(YELLOWGREEN, coord_triangle[count_players])

                    if event.key == pygame.K_KP_ENTER or \
                            event.key == pygame.K_RETURN or \
                            event.key == pygame.K_SPACE:
                        print(f'pressing enter, count players: {count_players}')
                        show = False
                        self.__window.fill(BLACK)
                    # exit
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        count_players = 0
                        break
                if event.type == pygame.KEYUP:
                    # exit
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        count_players = 0
                        break
            # update and delay
            clock.tick(FPS)
            pygame.display.update()
        return count_players

    def write_text(self, text: str,
                   coord: tuple,
                   size: int,
                   color=WHITE,
                   font='arial',
                   bckgnd_clr = BLACK,
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
        txt = f.render(text, True, color, bckgnd_clr)
        self.__window.blit(txt, coord)

    def paint_triangle(self, color: tuple, coord) -> None:
        """
        Нарисовать закрашенный треугольник
        :param color: цвета из модуля color
        :param coord: координаты вершин в формате кортежа (x,y)
        :return:
        """
        pygame.draw.polygon(self.__window, color, coord)

    def show_round_number(self, round_num: int) -> None:
        self.__window.fill(GRAY)
        self.write_text(text=str(round_num),
                        coord=(self.get_window_size()[0] / 2, self.get_window_size()[1] / 2),
                        size=40,
                        color=BLACK,
                        bckgnd_clr=GRAY
                        )
        clock = pygame.time.Clock()
        show = True
        while show:
            # ----------events---------------
            for event in pygame.event.get():
                # exit
                if event.type == pygame.QUIT:
                    show = False
                    exit(1)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP_ENTER or \
                            event.key == pygame.K_RETURN or \
                            event.key == pygame.K_SPACE:
                        show = False
                        self.__window.fill(BLACK)
                    # exit
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        break
            clock.tick(FPS)
            pygame.display.update()

    def show_game_window(self, tank_p1: BaseTank, tank_p2:BaseTank):
        """
        Метод обрабатывающий действие игрока на игровом поле
        :return: True-игра проиграна, False - игра идёт далее следующий раунд.
        """
        self.__window.fill(BLACK)
        clock = pygame.time.Clock()
        game_over = False
        round_over = False
        shoot_delay = 700
        while not round_over or not GAME_MECHANICS.round_over():
            # -------continued events (moving)---------
            keys = pygame.key.get_pressed()
            # Player 1
            if keys[pygame.K_UP]:
                tank_p1.up()
            elif keys[pygame.K_DOWN]:
                tank_p1.down()
            elif keys[pygame.K_LEFT]:
                tank_p1.left()
            elif keys[pygame.K_RIGHT]:
                tank_p1.right()
            if keys[pygame.K_SLASH]:
                tank_p1.shoot()
                sleep(shoot_delay)
            # Player 2
            if keys[pygame.K_w]:
                pass
            elif keys[pygame.K_s]:
                pass
            elif keys[pygame.K_a]:
                pass
            elif keys[pygame.K_d]:
                pass
            if keys[pygame.K_b]:
                pass
            # ----------one-shot events-----------------
            for event in pygame.event.get():
                # exit
                if event.type == pygame.QUIT:
                    round_over = True
                    exit(0)
                if event.type == pygame.KEYDOWN:
                    # Player 1 one-shot shoot
                    if event.key == pygame.K_PERIOD:
                        tank_p1.shoot()
                        sleep(shoot_delay)
                    # Player 2 one-shot shoot
                    if event.key == pygame.K_v:
                        pass
                    # common
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        break
                    if event.key == pygame.K_KP_ENTER or \
                            event.key == pygame.K_RETURN:
                        pass
            # update and delay
            GAME_MECHANICS.update()
            clock.tick(FPS)
            pygame.display.update()
        return game_over

    def show_statistics(self):
        pass

    def show_game_over(self):
        pass

    def get_window_size(self) -> tuple:
        """
        Метод возвращающий размер окна
        @todo сделать запрос текущего размера окна, тк окно может меняться в размерах
        :return:
        """
        return HEIGTH, WIDTH

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
