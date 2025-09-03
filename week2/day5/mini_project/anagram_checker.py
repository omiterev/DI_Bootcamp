import os
import random

dir_path = os.path.dirname(os.path.realpath(__file__))

class AnagramChecker:
    def __init__(self,file_path):
        with open(f'{dir_path}\{file_path}', 'r', encoding="utf-8") as f:
            self.words=[word.strip().lower() for word in f]
    def is_valid_word(self, word):
        if word.lower().strip() in self.words:
            return True
        else:
            return False
    def get_anagrams(self,word):
        anagrams=[]
        user_word=word.lower().strip()
        u_word_s=sorted(user_word)
        for lword in self.words:
            sorted_word=sorted(lword)
            if sorted_word==u_word_s and lword!=user_word:
                anagrams.append(lword)
        return anagrams



