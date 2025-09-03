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
        if name.strip() == 'Luke':
            name=name.strip()
            skywalker.append(f'{name} Skywalker\n')
        else:
            skywalker.append(name)
with open(f'{dir_path}\star_wars.txt','w',encoding = 'utf-8' ) as f:
    f.seek(0)
    f.writelines(skywalker)