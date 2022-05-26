"""
    Основной модуль с которого запускается игра
"""
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from player import PlayerParameters
from window import Window
from GameSequence.game_mechanics import GameMechanics, GAME_MECHANICS
PLAYER1 = None
PLAYER2 = None
CURR_ROUND_P1 = None
CURR_ROUND_P2 = None

# ----------------main-------------------------------
if __name__ == '__main__':
    window = Window(window_title="2D new tanks game", icon='images/logo.png')
    window.show_start_window()
    count_players = window.show_menu()
    if not count_players:
        exit(1)
    # handling choose gamer after press 'Enter' button
    elif count_players == 1:
        PLAYER1 = PlayerParameters()
    elif count_players == 2:
        PLAYER1 = PlayerParameters()
        PLAYER2 = PlayerParameters()
    else:
        print(f'\t\tERROR!\nВыбрано игроков: {count_players}\nВыход')
        exit(1)
    GAME_MECHANICS = GameMechanics()
    # game
    game_over = False
    while not game_over:
        GAME_MECHANICS.next_round()
        CURR_ROUND_P1 = PLAYER1.copy_for_curr_round()
        CURR_ROUND_P2 = PLAYER2.copy_for_curr_round() if count_players==2 else None
        window.show_round_number(GAME_MECHANICS.round_num)
        # game_over = window.show_game_window(CURR_ROUND_P1.tank, CURR_ROUND_P2.tank)
        # PLAYER1.add_prev_round(CURR_ROUND_P1)
        # PLAYER2.add_prev_round(CURR_ROUND_P2)
        # if not game_over:
        #     window.show_statistics()
    # game over
    else:
        window.show_game_over()
        window.show_statistics()
        window.show_game_over()
    exit(0)
