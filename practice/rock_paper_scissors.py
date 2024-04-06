# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 15:36:32 2022

@author: Anoop Maurya
"""

import random


def play():
    user=input("'r' for rock,'p' for paper,'s' for scissors \n")
    computer=random.choice(['r','p','s'])
    
    if user==computer:
        return 'It\'s a tie'
    
    if is_win(user,computer):
        return 'You won!'
    
    return 'You lost!'



def is_win(player,opponet):
    
    if(player=='r'and player=='s') or (player == 's' and opponet == 'p') or (player == 'p' and opponet == 'r'):
        return True
     
        
print(play())
    
    
    