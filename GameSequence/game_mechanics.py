#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from GameSequence.tank_field import Map

PLAYER1_RESPAWN = (0, 0)
PLAYER2_RESPAWN = (0, 0)
GAME_MECHANICS = None


class GameMechanics:
    def __init__(self) -> object:
        self.__round = 0
        self.__round_over = False
        self.__game_over = False

    def update(self):
        pass

    def bullet_coord(self):
        pass

    def tank_coord(self):
        pass

    def new_bullet(self):
        pass

    @property
    def round_over(self) -> bool:
        return self.__round_over

    @property
    def game_over(self) -> bool:
        return self.__game_over

    @property
    def round_num(self) -> int:
        return self.__round

    def next_round(self):
        """

        :param round:
        :return:
        """
        self.__round += 1
        self.__map = Map()
        self.__map.load(self.__round)
