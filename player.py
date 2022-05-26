"""
    Модуль с классами хранения данных об игроке
"""
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy

import GameSequence.tanks
from GameSequence.game_mechanics import PLAYER1_RESPAWN, PLAYER2_RESPAWN


class PlayerParameters_CurrRound:
    """
    Класс описывающий параметры одного игрока в текущем раунде
    """

    def __init__(self, number_player: int, lifes=3):
        if 0 < number_player <= 2:
            self.__score = 0
            self.__tanks_distroyed = 0
            self.__base_tanks_distroyed = 0
            self.__light_tanks_distroyed = 0
            self.__medium_tanks_distroyed = 0
            self.__havy_tanks_distroyed = 0
            self.__number_player = number_player
            self.__lifes = lifes
            self.__tank = GameSequence.tanks.BaseTank(
                player1=True if number_player == 1 else False,
                player2=True if number_player == 2 else False,
                coord=PLAYER1_RESPAWN if number_player == 1 else PLAYER2_RESPAWN
            )

    # score
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.score = score
        return self.score

    # tanks_distroyed
    @property
    def tanks_distroyed(self):
        return self.__tanks_distroyed

    @tanks_distroyed.setter
    def tanks_distroyed(self, tank):
        self.__tanks_distroyed = tank

    # base_tanks_distroyed
    @property
    def base_tanks_distroyed(self):
        return self.__base_tanks_distroyed

    @base_tanks_distroyed.setter
    def base_tanks_distroyed(self, tank):
        self.__base_tanks_distroyed = tank

    # light_tanks_distroyed
    @property
    def light_tanks_distroyed(self):
        return self.__light_tanks_distroyed

    @light_tanks_distroyed.setter
    def light_tanks_distroyed(self, tank):
        self.__light_tanks_distroyed = tank

    # medium_tanks_distroyed
    @property
    def medium_tanks_distroyed(self):
        return self.__medium_tanks_distroyed

    @medium_tanks_distroyed.setter
    def medium_tanks_distroyed(self, tank):
        self.__medium_tanks_distroyed = tank

    # havy_tanks_distroyed
    @property
    def havy_tanks_distroyed(self):
        return self.__havy_tanks_distroyed

    @havy_tanks_distroyed.setter
    def havy_tanks_distroyed(self, tank):
        self.__havy_tanks_distroyed = tank

    @property
    def lifes(self):
        return self.__lifes

    @lifes.setter
    def lifes(self, life):
        self.__lifes = life

    @property
    def number_player(self):
        return self.__number_player

    @property
    def tank(self):
        return self.__tank

    def __deepcopy__(self, memo):
        my_copy = type(self)(self.number_player)
        memo[id(self)] = my_copy
        my_copy.base_tanks_distroyed = copy.deepcopy(self.base_tanks_distroyed, memo)
        my_copy.havy_tanks_distroyed = copy.deepcopy(self.havy_tanks_distroyed, memo)
        my_copy.lifes = copy.deepcopy(self.lifes, memo)
        my_copy.light_tanks_distroyed = copy.deepcopy(self.light_tanks_distroyed, memo)
        my_copy.medium_tanks_distroyed = copy.deepcopy(self.medium_tanks_distroyed, memo)
        my_copy.score = copy.deepcopy(self.score, memo)
        my_copy.tanks_distroyed = copy.deepcopy(self.tanks_distroyed, memo)
        return my_copy


class PlayerParameters(PlayerParameters_CurrRound):
    """
    Класс описывающий параметры одного игрока во всей игре
    """
    COUNT_PLAYERS = 0

    def __init__(self):
        PlayerParameters.COUNT_PLAYERS += 1
        if PlayerParameters.COUNT_PLAYERS <= 2:
            PlayerParameters_CurrRound.__init__(self, PlayerParameters.COUNT_PLAYERS)

    def copy_for_curr_round(self):
        """
        Метод возвращает объект родительского класса с копией некоторых данных
        :return: Копирует данные:
                * number_player
                * lifes
                * round
        """
        copy = PlayerParameters_CurrRound(self.number_player)
        copy.lifes = self.lifes
        return copy

    def add_prev_round(self, prev_round: PlayerParameters_CurrRound) -> None:
        """
        Метод добавляет к общему счёту результаты прошедшего раунда
        :param other:
        :return:
        """
        self.round += 1
        self.lifes = prev_round.lifes
        self.score += prev_round.score
        self.tanks_distroyed += prev_round.tanks_distroyed
        self.base_tanks_distroyed += prev_round.base_tanks_distroyed
        self.light_tanks_distroyed += prev_round.light_tanks_distroyed
        self.medium_tanks_distroyed += prev_round.medium_tanks_distroyed
        self.havy_tanks_distroyed += prev_round.havy_tanks_distroyed
