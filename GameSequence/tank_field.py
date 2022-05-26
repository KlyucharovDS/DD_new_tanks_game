#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Map:

    def __init__(self):
        pass

    def load(self, round: int):
        """
        load new card from file
        :param round: round number
        :return: None
        """
        pass

    def get_object(self, coord: tuple):
        """
        Return available object on coordinates
        :param coord: coordinate
        :return: True/False
        """
        pass

    def hit(self, coord: tuple, damage:int):
        """
        Damage map object
        :param coord: coordinate bullet
        :param damage: damage bullet
        :return:
        """
        pass
