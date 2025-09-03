from anagram_checker import AnagramChecker
import os
import random

checker=AnagramChecker('sowpods.txt')
while True:
    user_word=input('Plese enter a word for anagram or "exit": ')
    if user_word=='exit':
        break
    elif checker.is_valid_word(user_word):
        print(f'Your word is: {user_word}\n')
        print('This is a valid English word.\n')
        print(f'Anagrams for your word: {" ,".join(checker.get_anagrams(user_word))}.\n')
        
    else:
        print('Invalid word\n')

        
