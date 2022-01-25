# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 03:56:33 2022

@author: Gyuchan
"""
results_file = open('results.txt', 'r')
for line in results_file.read().splitlines():
    result = line.split(',')
    print('Player win = {}'.format(int(result[2])+int(result[3])))
    print('Player win = {}'.format(int(result[0])+int(result[4])))
    print('Draw = {}'.format(int(result[1])))
results_file.close()

# game_stats = {
#     'p_bust':0,
#     'draw':0,
#     'd_bust':0,
#     'p_win':0,
#     'd_win':0
#     }
# print(game_stats)
# str_format = ""
# for key in game_stats:
#     str_format+=key+','
# print(str_format[:-1])