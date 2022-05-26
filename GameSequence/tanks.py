#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from GameSequence.game_mechanics import PLAYER1_RESPAWN, PLAYER2_RESPAWN


class Tank:
    """
    Класс описывающий общую модель танка и его основные функции
    """
    # общее число танков на поле
    __COUNT_TANKS_ON_FIELD = 0

    def __init__(self, *, player1=False, player2=False, tank_speed: int, hp: int, bullet_speed: int, penetration: int,
                 damage: int, coord: tuple):
        """
        Инициализация класса.
        :param tank_speed: Скорость танка от 1 по 10
        :param hp: живучесть(очки прочности, HP, Health Point) от 1 по 10
        :param bullet_speed: скорость пули от 1 по 10
        :param penetration: бронепробиваемость от 1 до 10
        :param damage: урон по противнику отнимающий очки здоровья от 1 до 10
        """
        Tank.__COUNT_TANKS_ON_FIELD += 1
        self.__tank_speed = tank_speed
        self.__hp = hp
        self.__bullet_speed = bullet_speed
        self.__penetration = penetration
        self.__damage = damage
        # точка респауна игроков
        if player1:
            self.__coord = PLAYER1_RESPAWN
            self.__course = {'UP': 1, 'DOWN': 0, 'LEFT': 0, 'RIGHT': 0}
        elif player2:
            self.__coord = PLAYER2_RESPAWN
            self.__course = {'UP': 1, 'DOWN': 0, 'LEFT': 0, 'RIGHT': 0}
        # точки респауна  ботов
        else:
            self.__coord = coord
            self.__course = {'UP': 0, 'DOWN': 1, 'LEFT': 0, 'RIGHT': 0}

    def up(self):
        pass

    def down(self):
        pass

    def left(self):
        pass

    def right(self):
        pass

    def shoot(self):
        pass

    def hit(self, damage):
        pass

    @staticmethod
    def get_count_tanks():
        return Tank.__COUNT_TANKS_ON_FIELD


class BaseTank(Tank):

    def __init__(self, *, player1=False, player2=False, coord: tuple):
        Tank.__init__(self, player1=player1, player2=player2,
                      tank_speed=1,
                      hp=1,
                      bullet_speed=1,
                      penetration=1,
                      damage=1,
                      coord=coord)


class LightTank(BaseTank):
    def __init__(self, *, player1=False, player2=False, coord: tuple):
        Tank.__init__(self, player1=player1, player2=player2,
                      tank_speed=7,
                      hp=1,
                      bullet_speed=7,
                      penetration=1,
                      damage=1,
                      coord=coord)


class MediumTank(BaseTank):
    def __init__(self, *, player1=False, player2=False, coord: tuple):
        Tank.__init__(self, player1=player1, player2=player2,
                      tank_speed=5,
                      hp=5,
                      bullet_speed=5,
                      penetration=5,
                      damage=5,
                      coord=coord)


class HeavyTank(BaseTank):
    def __init__(self, *, player1=False, player2=False, coord: tuple):
        Tank.__init__(self, player1=player1, player2=player2,
                      tank_speed=1,
                      hp=8,
                      bullet_speed=1,
                      penetration=7,
                      damage=7,
                      coord=coord)
