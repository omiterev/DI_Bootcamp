import random
class Game:
    def __init__(self):
        self.walid_answer=['rock','paper','scissors']
    
    def get_user_item(self):
        while True:
            user_answer=input('Please chose rock/paper/scissors: ').lower()
            if user_answer in self.walid_answer:
                return user_answer
            else:
                print('Invalid input\n')

    def get_computer_item(self):
        index=random.randint(0,2)

        return self.walid_answer[index]
    def get_game_result(self,user_item, computer_item):
        rules = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
        if rules[user_item]==computer_item:
            return 'win'
        elif user_item==computer_item:
            return 'draw'
        else:
            return 'loss'
    def play(self):
        user_item=self.get_user_item()
        comp_item=self.get_computer_item()
        result=self.get_game_result(user_item,comp_item)
        print(f'User\'s choice is {user_item}')
        print(f'Computer\'s choice is {comp_item}')
        print(f'Result is {result}\n')
        return result

        
