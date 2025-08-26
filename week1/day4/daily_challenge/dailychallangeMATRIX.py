matrix_str = '''
7ir
Tsi
h%x
i ?
sM#
$a 
#t%'''
D2_list=[]
rows = [row for row in matrix_str.split("\n") if row]
print(rows)
D2_list = [list(row) for row in rows]
# help_list=[]
# for l in matrix_str:
#     if l !="\n":
#         help_list.append(l)
#     elif l=="\n":
#          if help_list:
#             D2_list.append(help_list)
#             help_list=[]
# if help_list:
#     D2_list.append(help_list)
# print(D2_list)

matrix=''
row=len(D2_list)
col=len(D2_list[0])
for c in range(col):
    for r in range(row):
        matrix+=D2_list[r][c]
print(matrix)

matrix2=''
for c in range(col):
    for r in range(row):
        if D2_list[r][c].isalpha():
            matrix2+=D2_list[r][c]
print(matrix2)

matrix3=''
for c in range(col):
    for r in range(row):
        if D2_list[r][c].isalpha():
            matrix3+=D2_list[r][c]
        else:
            if D2_list[r-1][c].isalpha():
                 matrix3+=' '
matrix3 = matrix3.strip()
print(matrix3)