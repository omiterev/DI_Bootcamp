# [*******************]
# [*   x |  o  | o   *]
# [* ----|-----|---- *]
# [*     |  x  | x   *]
# [* ----|-----|---- *]
# [*     |     | x   *]
# [*******************]
g=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
def display_board():
    print('*******************')
    print(f'*   {g[0][0]} |  {g[0][1]}  | {g[0][2]}   *')
    print('* ----|-----|---- *')
    print(f'*   {g[1][0]} |  {g[1][1]}  | {g[1][2]}   *')
    print('* ----|-----|---- *')
    print(f'*   {g[2][0]} |  {g[2][1]}  | {g[2][2]}   *')
    print('*******************\n')

def player_input(player0):
    ran=['1','2','3']
    flag_empty=False
    while flag_empty==False:
        row_inp=input('Enter row: ')
        while row_inp not in ran:
            print('Wrong row, try again')
            row_inp=input('Enter row: ')
        col_inp=input('Enter column: ')
        while col_inp not in ran:
            print('Wrong column, try again')
            col_inp=input('Enter column: ')
        row=int(row_inp)-1
        col=int(col_inp)-1
        if g[row][col]!=' ':
            print('This cell is alredy occupied. Try again')
        else:
            flag_empty=True
    g[row][col]=player0
    return row, col

def check_win_tie(player0='i'): #board, player
    game_flag=False
    r1=g[0][0]
    r2=g[0][1]
    r3=g[0][2]
    r4=g[1][0]
    r5=g[1][1]
    r6=g[1][2]
    r7=g[2][0]
    r8=g[2][1]
    r9=g[2][2]
    if r1==r2==r3!=' ' or r4==r5==r6!=' ' or r7==r8==r9!=' ' or r1==r4==r7!=' ' or r2==r5==r8!=' ' or r3==r6==r9!=' ' or r1==r5==r9!=' ' or r3==r5==r7!=' ':
        game_flag=True
        print(f'\nPlayer {player0} WON!')
        return game_flag
    elif r1!=' ' and r2!=' ' and r3!=' ' and r4!=' ' and r5!=' ' and r6!=' ' and r7!=' ' and r8!=' ' and r9!=' ':
        game_flag=True
        print('\nTie')
        return game_flag
    else:
        return game_flag

game_flag=False
player1='X'
player2='O'
player=''
turn_count=1
want_play=True

print('Welcome to Tic Tac Toe!\n')
while want_play==True:
    while game_flag==False:
        display_board()
        if turn_count%2==0:
            player=player2
            turn_count+=1
        else:
            player=player1
            turn_count+=1
        print(f'Player {player}\'s turn ...')
        player_input(player)
        game_flag=check_win_tie(player)
        if game_flag==True:
            display_board()
    yes_no=input(f'Do you want to play one more time?(yes/no): ')
    if yes_no.lower()=='no':
        want_play=False
    elif yes_no.lower()=='yes':
        g=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        turn_count = 1
        game_flag=False
    else:
        print('Invalid command')
        want_play=False