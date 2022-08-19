import os 
os.system('cls')



win1 =0  
win2 = 0  
equal1 = 0 
equal2 = 0
lose1 = 0
lose2 = 0
score1  = 0 
score2 = 0
final_score1= 0 
final_score2 = 0
print ("\033[1;37mscore Table : \nwin = 3  equal = 1   lose = 0 " )


for i in range (1,6):   
     
         for j in range (2,6):
            away_game = "Away Game" 
            score1 = int(input ( "Enter the scores of Team-" + str(i)+" in the game with Team-" + str(j) + " in "+away_game+":" ) )
            
            if((score1 == 0) or (score1 == 1) or (score1 == 3)):
                final_score1 += score1

                if (score1 == 3):
                    win1 += 1
                elif (score1 == 1):
                     equal1 += 1
                elif (score1 == 0):
                    lose1 += 1
            else:
                print("Lets check the score table !! \ntry it again.")

     
            
         for z in range (2,6):
            home_game = "home Game"

            score2 = int(input ( "Enter the scores of Team-" + str(i)+" in the game with Team-" + str(z) + " in "+home_game + ":" ) )

            if((score2 ==0) or (score2 ==1) or (score2 ==3)):
                final_score2 += score2

                if (score2 == 3):
                    win2 += 1
                elif (score2 == 1):
                     equal2 += 1
                elif (score2 == 0):
                    lose2 += 1
            else:
                 print("Lets check the score table !! \ntry it again.")

         total_final_score = final_score1+final_score2
         total_win = win1 + win2 
         total_lose = lose1 + lose2 
         total_equal = equal1 + equal2

         print('total score in home Game :\nfinal_score   win   equal   loss\n','  ',total_final_score,'       ',total_win,'    ',total_equal,'    ',total_lose)         