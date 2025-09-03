import os
import random
dir_path = os.path.dirname(os.path.realpath(__file__))
#file_path=f'{dir_path}\words.txt'

def get_words_from_file(file_path):
    word_list=[]
    with open(f'{dir_path}\{file_path}', 'r', encoding="utf-8") as f:
        for line in f:
            for word in line.split():
                word_list.append(word.strip())
    return word_list

def get_random_sentence(sentence_length):
    sentence=''
    word_list=get_words_from_file('words.txt')
    list_length=len(word_list)
    for number in range(sentence_length):
        rundom_number=random.randint(0,list_length-1)
        sentence+=word_list[rundom_number]+' '
    return sentence

def main():
    print("This function returns a random sentence with given number of words.")
    try:
        sentence_length=int(input("Please enter a sentence length: "))
        if 2<=sentence_length<=20:
            sentence=get_random_sentence(sentence_length)
            print(sentence)
        else:
            raise ValueError('Nomber shold be from 2 to 20')
    except ValueError as e:
        print(ValueError, e)

main()