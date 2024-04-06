# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 07:58:20 2022

@author: Anoop Maurya
"""

import math
import random
#from game import TicTacToe


class Player:
    def __init__(self,letter):
        #letter is x or o
        self.letter=letter
        
    def get_moves(self,game):
        pass
    
    
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_moves(self,game):
        square=random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    
    def get_moves(self,game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9):')
            # we're going to check that this is a correct value by trying to cast
            # it to an integer, and if it's not, then we say its invalid
            # #if that spot is nit availabel on the board, we also say its invalid
            try:
                val=int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square= True  # if these are succesfull
            except ValueError:
                print("Invalid square. Try again. ")

        return val




    