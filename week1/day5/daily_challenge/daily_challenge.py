#1
def sort_string(words:str)-> str:
    '''Clean and sort user words'''
    user_list=[word.strip() for word in words.split(',')]
    sorted_list=sorted(user_list)
    sorted_str=",".join(sorted_list)
    return sorted_str
user_str=input('Enter words, separeted by commas: ')
print(sort_string(user_str))
#2
user_sentence=input('Enter your sentence: ')

def longest_word(sentence:str)-> str:
    '''Return the longest word in sentence'''
    word_list=sentence.split()
    longest_word=word_list[0]
    for  word in word_list:
        if len(word)>len(longest_word):
            longest_word=word
    return longest_word
print(longest_word(user_sentence))