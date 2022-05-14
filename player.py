#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class PlayerParameters_CurrRound:
    """
    Класс описывающий параметры одного игрока в текущем раунде
    """

    def __init__(self, number_player):
        if number_player <= 2:
            self.score = 0
            self.tanks_distroyed = 0
            self.base_tanks_distroyed = 0
            self.light_tanks_distroyed = 0
            self.medium_tanks_distroyed = 0
            self.havy_tanks_distroyed = 0
            self.number_player = number_player
            self.lifes = 3

    # score
    @property
    def score(self):
        return self.score

    @score.setter
    def score(self, score):
        self.score += score
        return self.score

    # tanks_distroyed
    @property
    def tanks_distroyed(self):
        return self.tanks_distroyed

    @tanks_distroyed.setter
    def tanks_distroyed(self, tank):
        self.tanks_distroyed += tank

    # base_tanks_distroyed
    @property
    def base_tanks_distroyed(self):
        return self.tanks_distroyed

    @base_tanks_distroyed.setter
    def base_tanks_distroyed(self, tank):
        self.base_tanks_distroyed += tank

    # light_tanks_distroyed
    @property
    def light_tanks_distroyed(self):
        return self.light_tanks_distroyed

    @light_tanks_distroyed.setter
    def light_tanks_distroyed(self, tank):
        self.light_tanks_distroyed += tank

    # medium_tanks_distroyed
    @property
    def medium_tanks_distroyed(self):
        return self.medium_tanks_distroyed

    @medium_tanks_distroyed.setter
    def medium_tanks_distroyed(self, tank):
        self.medium_tanks_distroyed += tank

    # havy_tanks_distroyed
    @property
    def havy_tanks_distroyed(self):
        return self.havy_tanks_distroyed

    @havy_tanks_distroyed.setter
    def havy_tanks_distroyed(self, tank):
        self.havy_tanks_distroyed += tank

    @property
    def lifes(self):
        return self.lifes

    @lifes.setter
    def lifes(self, life):
        self.lifes += life

    @property
    def number_player(self):
        return self.number_player


class PlayerParameters(PlayerParameters_CurrRound):
    """
    Класс описывающий параметры одного игрока во всей игре
    """
    COUNT_PLAYERS = 0

    def __init__(self):
        PlayerParameters.COUNT_PLAYERS += 1
        if PlayerParameters.COUNT_PLAYERS <= 2:
            PlayerParameters_CurrRound.__init__(self, PlayerParameters.COUNT_PLAYERS)