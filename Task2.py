import random

list_choice = ['rock', 'paper', 'scissors']
score = [['user', 0], ['computer', 0]]

def rockyou(user_choice):
    user_win = ''
    com_choice = random.choice(list_choice)
    print('com choice = ', com_choice)
    if user_choice == com_choice:
        return 'equal'
    if user_choice == 'rock':
        if com_choice == 'scissors':
            score[0][1] += 1
            return True
        else:
            score[1][1] += 1
            return False
    if user_choice == 'paper':
        if com_choice == 'rock':
            score[0][1] += 1
            return True
        else:
            score[1][1] += 1
            return False
    if user_choice == 'scissors':
        if com_choice == 'paper':
            score[0][1] += 1
            return True
        else:
            score[1][1] += 1
            return False


while score[0][1] < 3:
    res = rockyou(input('rock paper or scissors? : '))
    res = "You!!!" if res == True else "PC" if res == False else 'equal'
    print('who is the winner? : ', res)
print('static: ', score)

