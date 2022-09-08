import random 
from tabulate import tabulate
from termcolor import colored



choices = ['r', 'p', 's']
info = {'option': ['single player', 'double player'] ,'Your choice:': ['11', '12' ] }
print(colored(tabulate(info, headers='keys', tablefmt='fancy_grid') , 'blue') )

option = int(input("Now Enter your option :"))

info1 = [['Game round :'] ,['1) 1 round '], ['2) 3 round '],['3) 5 round ']]
print(colored(tabulate(info1, tablefmt='fancy_grid') , 'cyan') )
   
round = int(input("Then Enter the score you want to game end  :"))

computer_score = 0
player_score = 0
round_counter1 = 0
round_counter2 = 0
user1_score=0
user2_score=0


while True:
 
    if round == 1 :

            
        if option == 11  :
            ai_choice = random.choice(choices)
            user_choice = input('\033[1;36m'+"Enter your Choice (r=Rock / p=Paper  / s=Scissors) :"+'\033[0m')
            print ("\033[1;31m"+f'Ai choice: {ai_choice}')
            print ("\033[1;32m"+f'User choice: {user_choice}' +'\033[0m')
        
        #  halat haei k user mibare p>r  r>s  s>p
            if ai_choice == user_choice:
                print (colored("Its a tie." , 'yellow'))
                info = {'players': ['AI', 'user'] ,'score:': [computer_score , player_score ] }
                print(colored(tabulate(info, headers='keys', tablefmt='fancy_grid'), 'yellow') )
                continue

            elif user_choice == 'p'  and  ai_choice == 'r':
                print ("You wins.")
                player_score+=1
                info = {'players': ['AI', 'user'] ,'score:': [computer_score , player_score ] }
                print(colored(tabulate(info, headers='keys', tablefmt='fancy_grid'), 'green') )
                break
                

            elif user_choice == 'r'  and  ai_choice == 's':
                print ("You wins.")
                player_score+=1
                info = {'players': ['AI', 'user'] ,'score:': [computer_score , player_score ] }
                print(colored(tabulate(info, headers='keys', tablefmt='fancy_grid') , 'green'))
                break  

            elif user_choice == 's'  and  ai_choice == 'p':
                print ("You wins.")
                player_score+=1
                info = {'players': ['AI', 'user'] ,'score:': [computer_score , player_score] }
                print(colored(tabulate(info, headers='keys', tablefmt='fancy_grid') , 'green') )
                break

            else :
                print ("I win , You Lost!.")
                computer_score+=1
                info = {'players': ['AI', 'user'] ,'score:': [computer_score , player_score ] }
                print(colored(tabulate(info, headers='keys', tablefmt='fancy_grid') , 'red') )
                break

        # 2nafare -> point 
        
        elif option == 12  and (round == 1  or round == 3 or round == 5):
            
            user1_choice = input("\033[1;32m"+"Enter your Choice (r=Rock / p=Paper  / s=Scissors): " + "\033[0m")
            user2_choice = input("\033[1;31m" + "Enter your Choice (r=Rock / p=Paper  / s=Scissors): " + "\033[0m")
            print ("\033[1;32m"+ f'user1 choice: {user1_choice}' + "\033[0m")
            print ("\033[1;31m" + f'User2 choice: {user2_choice}' + "\033[0m")
        
        #  halat haei k user2 mibare p>r  r>s  s>p

            if user1_choice == user2_choice:
                print ("Its a tie.")
                info = {'players': ['user1', 'user2'] ,'score:': [user1_score , user2_score ] }
                print(colored(tabulate(info, headers='keys', tablefmt='fancy_grid') , 'yellow') )
                continue   
        
                

            elif user2_choice == 'p'  and  user1_choice == 'r':
                print ("User2 wins.")
                user2_score+=1
                info = {'players': ['user1', 'user2'] ,'score:': [user1_score , user2_score ] }
                print(colored (tabulate(info, headers='keys', tablefmt='fancy_grid') , 'red') )
                break

            elif user2_choice == 'r'  and user1_choice == 's':
                print ("User2 wins.")
                user2_score+=1
                info = {'players': ['user1', 'user2'] ,'score:': [user1_score , user2_score ] }
                print( colored (tabulate(info, headers='keys', tablefmt='fancy_grid') , 'red') )
                break

            elif user2_choice == 's'  and  user1_choice == 'p':
                print ("User2 wins.")
                user2_score+=1
                info = {'players': ['user1', 'user2'] ,'score:': [user1_score , user2_score] }
                print(colored (tabulate(info, headers='keys', tablefmt='fancy_grid'), 'red') )
                break

            else :
                print ("user1 wins , You Lost! 'U+2639'.")
                user1_score+=1
                info = {'players': ['user1', 'user2'] ,'score:': [user1_score , user2_score ] }
                print(colored(tabulate(info, headers='keys', tablefmt='fancy_grid') , 'green') )
                break



        # Check Input Spelling...
        else:
            print("You entered unvalid number !!!. please check a guide table first.\n")
            continue

        # #for take next plays
        # ai_choice = random.choice(choices)
        # user_choice = input("Enter your Choice: (r=Rock / p=Paper  / s=Scissors) ")

    elif round == 2:

        if round_counter1 <3 and round_counter2 <3 :
        
            if option == 11 :
                ai_choice = random.choice(choices)
                user_choice = input('\033[1;36m'+"Enter your Choice (r=Rock / p=Paper  / s=Scissors) :"+'\033[0m')
                print ("\033[1;31m"+f'Ai choice: {ai_choice}')
                print ("\033[1;32m"+f'User choice: {user_choice}' +'\033[0m')
            
            #  halat haei k user mibare p>r  r>s  s>p
                if ai_choice == user_choice:
                    print (colored("Its a tie." , 'yellow'))
                    info = {'players': ['AI', 'user'] ,'score:': [computer_score , player_score ] }
                    print(colored(tabulate(info, headers='keys', tablefmt='fancy_grid'), 'yellow') )
                    continue

                elif user_choice == 'p'  and  ai_choice == 'r':
                    print ("You wins.")
                    player_score+=1
                    info = {'players': ['AI', 'user'] ,'score:': [computer_score , player_score ] }
                    print(colored(tabulate(info, headers='keys', tablefmt='fancy_grid'), 'green') )
                    round_counter1+=1
                    continue
                    
                    

                elif user_choice == 'r'  and  ai_choice == 's':
                    print ("You wins.")
                    player_score+=1
                    info = {'players': ['AI', 'user'] ,'score:': [computer_score , player_score ] }
                    print(colored(tabulate(info, headers='keys', tablefmt='fancy_grid') , 'green'))
                    round_counter1+=1
                    continue
                    

                elif user_choice == 's'  and  ai_choice == 'p':
                    print ("You wins.")
                    player_score+=1
                    info = {'players': ['AI', 'user'] ,'score:': [computer_score , player_score] }
                    print(colored(tabulate(info, headers='keys', tablefmt='fancy_grid') , 'green') )
                    round_counter1+=1
                    continue

                else :
                    print ("I win , You Lost!.")
                    computer_score+=1
                    info = {'players': ['AI', 'user'] ,'score:': [computer_score , player_score ] }
                    print(colored(tabulate(info, headers='keys', tablefmt='fancy_grid') , 'red') )
                    round_counter2+=1
            

            # 2nafare -> point 3
            
            elif option == 12 :
                
                user1_choice = input("\033[1;32m"+"Enter your Choice (r=Rock / p=Paper  / s=Scissors): " + "\033[0m")
                user2_choice = input("\033[1;31m" + "Enter your Choice (r=Rock / p=Paper  / s=Scissors): " + "\033[0m")
                print ("\033[1;32m"+ f'user1 choice: {user1_choice}' + "\033[0m")
                print ("\033[1;31m" + f'User2 choice: {user2_choice}' + "\033[0m")
            
            #  halat haei k user2 mibare p>r  r>s  s>p

                if user1_choice == user2_choice:
                    print ("Its a tie.")
                    info = {'players': ['user1', 'user2'] ,'score:': [user1_score , user2_score ] }
                    print(colored(tabulate(info, headers='keys', tablefmt='fancy_grid') , 'yellow') )
                    print( "\033[0;37m"+ f'Game score resualt => \nuser2:{round_counter2}  user1:{round_counter1}' +"\033[0m")
                     
            
                    

                elif user2_choice == 'p'  and  user1_choice == 'r':
                    print ("User2 wins.")
                    user2_score+=1
                    info = {'players': ['user1', 'user2'] ,'score:': [user1_score , user2_score ] }
                    print(colored (tabulate(info, headers='keys', tablefmt='fancy_grid') , 'red') )
                    round_counter2+=1
                    continue

                elif user2_choice == 'r'  and user1_choice == 's':
                    print ("User2 wins.")
                    user2_score+=1
                    info = {'players': ['user1', 'user2'] ,'score:': [user1_score , user2_score ] }
                    print( colored (tabulate(info, headers='keys', tablefmt='fancy_grid') , 'red') )
                    round_counter2+=1
                    continue

                elif user2_choice == 's'  and  user1_choice == 'p':
                    print ("User2 wins.")
                    user2_score+=1
                    info = {'players': ['user1', 'user2'] ,'score:': [user1_score , user2_score] }
                    print(colored (tabulate(info, headers='keys', tablefmt='fancy_grid'), 'red') )
                    round_counter2+=1
                    continue


                else :
                    print ("user1 wins , You Lost! 'U+2639'.")
                    user1_score+=1
                    info = {'players': ['user1', 'user2'] ,'score:': [user1_score , user2_score ] }
                    print(colored(tabulate(info, headers='keys', tablefmt='fancy_grid') , 'green') )
                    round_counter1+=1
                    print( "\033[0;37m"+ f'Game score resualt \nuser2:{round_counter2}  user1:{round_counter1}' +"\033[0m")
                    continue
        else:
            break            


            # Check Input Spelling...
    
    elif  round == 3:
    
        if round_counter1 <5 and round_counter2 <5 :
        
            if option == 11 :
                ai_choice = random.choice(choices)
                user_choice = input('\033[1;36m'+"Enter your Choice (r=Rock / p=Paper  / s=Scissors) :"+'\033[0m')
                print ("\033[1;31m"+f'Ai choice: {ai_choice}')
                print ("\033[1;32m"+f'User choice: {user_choice}' +'\033[0m')
            
            #  halat haei k user mibare p>r  r>s  s>p
                if ai_choice == user_choice:
                    print (colored("Its a tie." , 'yellow'))
                    info = {'players': ['AI', 'user'] ,'score:': [computer_score , player_score ] }
                    print(colored(tabulate(info, headers='keys', tablefmt='fancy_grid'), 'yellow') )
                    continue

                elif user_choice == 'p'  and  ai_choice == 'r':
                    print ("You wins.")
                    player_score+=1
                    info = {'players': ['AI', 'user'] ,'score:': [computer_score , player_score ] }
                    print(colored(tabulate(info, headers='keys', tablefmt='fancy_grid'), 'green') )
                    round_counter1+=1
                    continue
                    
                    

                elif user_choice == 'r'  and  ai_choice == 's':
                    print ("You wins.")
                    player_score+=1
                    info = {'players': ['AI', 'user'] ,'score:': [computer_score , player_score ] }
                    print(colored(tabulate(info, headers='keys', tablefmt='fancy_grid') , 'green'))
                    round_counter1+=1
                    continue
                    

                elif user_choice == 's'  and  ai_choice == 'p':
                    print ("You wins.")
                    player_score+=1
                    info = {'players': ['AI', 'user'] ,'score:': [computer_score , player_score] }
                    print(colored(tabulate(info, headers='keys', tablefmt='fancy_grid') , 'green') )
                    round_counter1+=1
                    continue

                else :
                    print ("I win , You Lost!.")
                    computer_score+=1
                    info = {'players': ['AI', 'user'] ,'score:': [computer_score , player_score ] }
                    print(colored(tabulate(info, headers='keys', tablefmt='fancy_grid') , 'red') )
                    round_counter2+=1
            

            # 2nafare -> point 3
            
            elif option == 12 :
                
                user1_choice = input("\033[1;32m"+"Enter your Choice (r=Rock / p=Paper  / s=Scissors): " + "\033[0m")
                user2_choice = input("\033[1;31m" + "Enter your Choice (r=Rock / p=Paper  / s=Scissors): " + "\033[0m")
                print ("\033[1;32m"+ f'user1 choice: {user1_choice}' + "\033[0m")
                print ("\033[1;31m" + f'User2 choice: {user2_choice}' + "\033[0m")
            
            #  halat haei k user2 mibare p>r  r>s  s>p

                if user1_choice == user2_choice:
                    print ("Its a tie.")
                    info = {'players': ['user1', 'user2'] ,'score:': [user1_score , user2_score ] }
                    print(colored(tabulate(info, headers='keys', tablefmt='fancy_grid') , 'yellow') )
                    print( "\033[0;37m"+ f'Game score resualt => \nuser2:{round_counter2}  user1:{round_counter1}' +"\033[0m")
                     
            
                    

                elif user2_choice == 'p'  and  user1_choice == 'r':
                    print ("User2 wins.")
                    user2_score+=1
                    info = {'players': ['user1', 'user2'] ,'score:': [user1_score , user2_score ] }
                    print(colored (tabulate(info, headers='keys', tablefmt='fancy_grid') , 'red') )
                    round_counter2+=1
                    continue

                elif user2_choice == 'r'  and user1_choice == 's':
                    print ("User2 wins.")
                    user2_score+=1
                    info = {'players': ['user1', 'user2'] ,'score:': [user1_score , user2_score ] }
                    print( colored (tabulate(info, headers='keys', tablefmt='fancy_grid') , 'red') )
                    round_counter2+=1
                    continue

                elif user2_choice == 's'  and  user1_choice == 'p':
                    print ("User2 wins.")
                    user2_score+=1
                    info = {'players': ['user1', 'user2'] ,'score:': [user1_score , user2_score] }
                    print(colored (tabulate(info, headers='keys', tablefmt='fancy_grid'), 'red') )
                    round_counter2+=1
                    continue


                else :
                    print ("user1 wins , You Lost! 'U+2639'.")
                    user1_score+=1
                    info = {'players': ['user1', 'user2'] ,'score:': [user1_score , user2_score ] }
                    print(colored(tabulate(info, headers='keys', tablefmt='fancy_grid') , 'green') )
                    round_counter1+=1
                    print( "\033[0;37m"+ f'Game score resualt \nuser2:{round_counter2}  user1:{round_counter1}' +"\033[0m")
                    continue
        else:
            break            


            # Check Input Spelling...
    else:
         print("You entered unvalid number !!!. please check a guide table first.\n")
         continue
        
        