import random

win_pair_dict = {}
computer_options = []
user_options = ['!exit', '!rating']
score_file = 'rating.txt'


def updateScore(fil, my_name, s):
    f = open(fil, 'r')
    lines = f.readlines()  # readlines
    found = False  # to check if names is in file
    for i, l in enumerate(lines):  # go through each line looking for name to edit line
        n, oldS = l.split()  # save the name and score in a var
        if n == my_name:
            s += int(oldS)  # add old score to new score
            lines[i] = my_name + ' ' + str(s) + '\n'  # change the line
            found = True  # update 'found'
            break  # exit for loop
    lines.append(my_name + ' ' + str(s) + '\n' if not found else '')  # add line with name if name not found
    f.close()

    f2 = open(fil, 'w+')
    f2.writelines(lines)  # write all lines back into file (replacing old lines)
    f2.close()
    return (s)  # return new score


def game(fil, my_name):


    rules = input()
    print("Okay, let's start")

    while True:
        if rules == '':
            rules = 'rock,paper,scissors'
        rules_list = rules.split(',')
        user_choice = input()
        computer_options.extend(rules_list)
        user_options.extend(rules_list)
        computer_choice = random.choice(computer_options)
        score = updateScore(fil, my_name, 0)
        if user_choice not in rules_list:
            if user_choice == '!exit':
                print('Bye!')
                break
            elif user_choice == '!rating':
                print("Your rating:", score)
            else:
                print('Invalid input')
        elif user_choice in rules_list:
            index_user_choice = rules_list.index(user_choice)
            new_list = rules_list[index_user_choice + 1:] + rules_list[:index_user_choice]
            index_slice = int(len(new_list) / 2)
            win_list = new_list[:index_slice]
            # loose_list = new_list[index_slice:]

            if user_choice in list(user_options):
                if user_choice == '!exit':
                    print('Bye!')
                    break
                elif user_choice == '!rating':
                    print("Your rating:", score)
                elif computer_choice in win_list:
                    print(f'Sorry, but the computer chose {computer_choice}')
                    score += updateScore(fil, my_name, 0)
                elif computer_choice == user_choice:
                    print(f'There is a draw ({computer_choice})')
                    score += updateScore(fil, my_name, 50)
                else:
                    print(f'Well done. The computer chose {computer_choice} and failed')
                    score += updateScore(fil, my_name, 100)

            else:
                print('Invalid input')








user_name = input('Enter your name: ')
print('Hello,', user_name)
game(score_file, user_name)
