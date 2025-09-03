import os
dir_path = os.path.dirname(os.path.realpath(__file__))
#old school

# try:
#     f=open('secret.txt')
#     secret_data=f.read()
#     print(secret_data)
# except:
#     raise ValueError
# finally:
#     f.close()

    
#Modern Way

# with open(f'{dir_path}\secret.txt','a+',encoding = 'utf-8' ) as f:
#     file_content=f.read()
#     print(file_content)
#     f.write('\nBla bla')
#     print("Content sucsessfuly added")

#with open(f'{dir_path}\star_wars.txt','r',encoding = 'utf-8' ) as f:
    #star_wars=f.read()
    # for r in star_wars:
    #     print(r.rstrip())
    # for i,line in enumerate(star_wars,1):
    #     if i==5:
    #         fifth=line.rstrip()
    #         break
    # print(fifth)
    # print(star_wars)
    # f.seek(0)
    # fifth_line=f.readline(5)
    # print(fifth_line)
    # f.seek(0)
    # letters_sw=f.read()
    # for i in range(1,5):
    # for line in f:
    #     print(f.readline())    
    #print(f.readlines()[9])

# with open(f'{dir_path}\star_wars.txt','r',encoding = 'utf-8' ) as f:
#     print(f.readline(5))
# with open(f'{dir_path}\star_wars.txt','r',encoding = 'utf-8' ) as f:
#     txt_content=f.readlines()
#     final_list=[]
#     for line in txt_content:
#         final_list.append(list(line))
#     print(final_list)

#     final_list=[list(line) for line in txt_content]
# with open(f'{dir_path}\star_wars.txt','r',encoding = 'utf-8' ) as f:
#     txt_content=f.readlines()
#     clean_list=[line.strip() for line in txt_content]
#     print(clean_list.count('Darth'))

# with open(f'{dir_path}\star_wars.txt','a',encoding = 'utf-8' ) as f:
#     f.write('\nOlga')

with open(f'{dir_path}\star_wars.txt','r',encoding = 'utf-8' ) as f:
    txt_content=f.readlines()
    skywalker=[]
    #clean_list=[line.strip() for line in txt_content]
    for name in txt_content:
        if name.strip()== 'Luke':
            name=name.strip()
            skywalker.append(f'{name} Skywalker\n')
        else:
            skywalker.append(name)
with open(f'{dir_path}\star_wars.txt','w',encoding = 'utf-8' ) as f:
    f.seek(0)
    f.writelines(skywalker)


# 1. Как читать файл построчно

# Это безопасно даже для больших файлов:

# with open("nameslist.txt", "r", encoding="utf-8") as f:
#     for line in f:            # перебираем по одной строке
#         print(line.strip())   # .strip убирает \n


# 👉 Такой способ не грузит весь файл в память. Для маленьких тоже можно, это универсально.

# 2. Прочитать только 5-ю строку

# Если файл небольшой, можно readlines() (он загружает всё в память):

# with open("nameslist.txt", "r", encoding="utf-8") as f:
#     lines = f.readlines()
#     print(lines[4].strip())   # индекс 4 = 5-я строка


# Если файл большой, лучше просто пройтись с enumerate:

# with open("nameslist.txt", "r", encoding="utf-8") as f:
#     for i, line in enumerate(f, start=1):
#         if i == 5:
#             print(line.strip())
#             break

# 3. Прочитать только первые 5 символов файла
# with open("nameslist.txt", "r", encoding="utf-8") as f:
#     first5 = f.read(5)
# print(first5)

# 4. Прочитать весь файл в список строк → разбить на буквы
# with open("nameslist.txt", " r", encoding="utf-8") as f:
#     lines = f.read().split()       # разобьёт по пробелам и \n
# letters = [list(word) for word in lines]   # каждое слово → список букв
# print(letters[:5])  # первые 5 для примера

# 5. Посчитать, сколько раз встречаются имена
# with open("nameslist.txt", "r", encoding="utf-8") as f:
#     text = f.read()

# print("Darth:", text.count("Darth"))
# print("Luke:", text.count("Luke"))
# print("Lea:", text.count("Lea"))

# 6. Добавить своё имя в конец файла
# with open("nameslist.txt", "a", encoding="utf-8") as f:
#     f.write("\nOlga")   # замените на своё имя

# 7. Добавить «SkyWalker» к каждому «Luke»

# Для этого нужно прочитать и переписать файл заново:

# with open("nameslist.txt", "r", encoding="utf-8") as f:
#     text = f.read()

# text = text.replace("Luke", "Luke SkyWalker")

# with open("nameslist.txt", "w", encoding="utf-8") as f:
#     f.write(text)

# 💡 Важный вывод

# Если файл маленький → можно смело использовать .read() или .readlines().

# Если файл большой → лучше идти построчно с for line in f: или с enumerate.