
#shart payan bazi 
#feacher ha mokhtalef 





import random
from tabulate import tabulate

print ( '\033[1m' + '---------- Welcome to Hnag man  ----------' + '\033[0m')

info = {'category:': ['Food', 'Color', 'Computer','Body','Animall','Subjects','Sports','Things','Vegetable','Nature','Places'],
'Your choice:': ['1', '2' ,'3','4','5','6','7','8','9','10','11']}
print(tabulate(info, headers='keys', tablefmt='fancy_grid') )
choice = int(input("we waiting for you .. :"))


foods = ['hamburger','Caesar Salad','pizza','sushi','hotdog','kebab','ghormesabzi',
'icecream','pasta','Beef Stroganoff','noodles','friedchicken']

colors= ['red', 'green','blue','black','purple','gray','yellow', 'white','violet','golden']

computer = ['monitor','mouse','controller','switch','speaker','keyboard','windows','stackoverflow']

Body = ['Throat','Forearm','Pancreas','tangue','shoulder','teeth','thumb','Elbow','Stomach','Brain']

animall = ['wolf','grasshoper','grollia','owl','butterfly','keyboard','eagle','caterpillar']

subjects = ['monitor','mouse','controller','switch','speaker','keyboard','windows','stackoverflow']

sports = ['basketball','swimming','soccer','chess','cycling','hockey','vollyball','bodybilding']

things = ['monitor','mouse','controller','switch','speaker','keyboard','windows','stackoverflow']

vegtebale = ['monitor','mouse','controller','switch','speaker','keyboard','windows','stackoverflow']

nature = ['monitor','mouse','controller','switch','speaker','keyboard','windows','stackoverflow']

places = ['monitor','mouse','controller','switch','speaker','keyboard','windows','stackoverflow']

final_answer = random.choice(foods)
wrong_list=[]
show_list=[]

dictionary=[]

for i in range (len(final_answer)):
        show_list.append('_')




while True:

    
    letter_user = input ("You letter : ")

    #inja miad check mikone ag harfe user ba string barabar nabod bebare to wrong list 

    if  final_answer.find(letter_user) == -1:
        wrong_list.append(letter_user)
       
    

    else :
        for i in range(len(final_answer)):
            if final_answer[i]== letter_user:
                show_list[i]= letter_user

            else :
                continue

    print ("wrong list" ,wrong_list )
    print(' '.join(show_list))



