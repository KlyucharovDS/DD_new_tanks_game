#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Tank:
    """
    Класс описывающий общую модель танка и его основные функции
    """
    __number = 0

    def __init__(self, tank_speed=1, strength=1, bullet_speed=1, penetration=1, damage=1, coord =(0,0)):
        """
        Инициализация класса.
        :param tank_speed: Скорость танка от 1 по 10
        :param strength: живучесть(очки прочности, HP, Health Point) от 1 по 10
        :param bullet_speed: скорость пули от 1 по 10
        :param penetration: бронепробиваемость, снятие очков здоровья от 1 по 10
        :param damage: урон по противнику отнимающий очки здоровья
        """
        Tank.__number += 1
        self.tank_speed = tank_speed
        self.strenght = strength
        self.bullet_speed = bullet_speed
        self.penetration = penetration
        self.damage = damage

    @staticmethod
    def get_count_tanks():
        return Tank.__number

