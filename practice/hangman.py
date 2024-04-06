# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 20:06:02 2022

@author: Anoop Maurya
"""

import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) #randomly chooses something from the list
    while '-' in word or ' ' in word :
        word = random.choice(words)
        
        
    return word

def hangman():
    word =get_valid_word(words)
    word_letters=set(word)
    alphabet=set(string.ascii_uppercase)
    used_letters=set()
    
    lives=6
    
    #getting user input
    while len(word_letters)>0 and lives > 0:
        #letters used
        # ''.join['a','b','cd']
        print("You have ",lives,"lives left and you have used these leters : ',' ".join(used_letters))
        user_letter=input("Guess a letter").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
            else:
                lives=lives-1 #takes away a life if worong
                
        elif user_letter in used_letters:
            print("You have already used that character. as try again")
            
            
        else:
            print("Invalid Character. Please try again ")
            
        
        if lives == 0:
            print("You have died .The word was ",word)
        else:   
            print("you have guessed the word",word,'!!')
            
            
            
    

user_input= input("Type Something :")
print(user_input)


hangman()
    
    
