from game import Game

def get_user_menu_choice():
    print('Menu options:\nPlay a new game\nShow scores\nQuit\n')
    while True:
        menu_options=['play a new game', 'show scores', 'quit']
        menu_choice=input('Please chose a menu option: ').lower()
        if menu_choice in menu_options:
            return menu_choice
        else:
            print('Invalid input')

def print_results(results):
    results_dict=results
    print(f"\nWins:{results_dict['win']}, Losses:{results_dict['loss']}, Draws:{results_dict['draw']}.")
    print('Thank you for playing\n')

def main():
    results_main={'win':0,'loss':0,'draw':0}
    while True:
        menu_option=get_user_menu_choice()
        if menu_option=='play a new game':
            game1=Game()
            result=game1.play()
            results_main[result]+=1
        elif menu_option=='show scores':
            print_results(results_main)
        elif menu_option=='quit':
            print_results(results_main)
            break

# if __name__ == "__main__":
#     main()

main()