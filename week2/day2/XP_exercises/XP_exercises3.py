class Person:
    def __init__(self,first_name,age,last_name:str=''):
        self.first_name=first_name
        self.age=age
        self.last_name=last_name
        pass
    def is_18(self):
        return self.age>18
     
           

class Family:
    def __init__(self,last_name):
        self.last_name=last_name
        self.members=[]
    def born(self,first_name, age:int):
        person=Person(first_name,age,self.last_name)
        return self.members.append(person)
    def check_majority(self,first_name):
        for person in self.members:
            if person.first_name == first_name:
                if person.is_18():
                    print('You are over 18, your parents Jane and John accept that you will go out with your friends')
                else:
                    print('Sorry, you are not allowed to go out with your friends.')
    def family_presentation(self):
        print(self.last_name)
        for person in self.members:
            print(person.first_name, person.age)



family1=Family('Smit')
family1.born('Jane',45)
family1.born('John',52)
family1.born('Luke',8)
family1.born('Nina',19)
family1.check_majority('Luke')
family1.check_majority('Nina')
family1.check_majority('Mike')
family1.family_presentation()