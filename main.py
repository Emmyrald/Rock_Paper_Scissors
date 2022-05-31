import random
def rps():
    start = input ("Press Y to begin: ").strip().capitalize()
    choices = ['R','P','S']
    choices_meaning = ['Rock','Paper','Scissors']
    while start == 'Y':
        while True:
            player_choice = input ('Select R for Rock, S for scissors and P for paper: ').strip().capitalize()
            if player_choice in choices:
                break
            else:
                print ('Invalid selection')
        cpu_choice = random.choice(choices)
        print ('Player(',choices_meaning[choices.index(player_choice)],') :', 'CPU (',choices_meaning[choices.index(cpu_choice)],')')
        if (player_choice =='R' and cpu_choice == 'S') or (player_choice == 'P' and cpu_choice == 'R') or (player_choice == 'S' and cpu_choice == 'P'):
            print ('Congratulations!!!\nPlayer wins')
            break
        elif player_choice == cpu_choice:
            print ('It\'s a draw \nTry again')
            continue
        else:
            print ("CPU wins!!!")
            break
rps()
