import random
l = ["rock","paper","scissor"]
'''
rock vs paper -> paper wins
rock vs scissor -> rock wins
paper vs scissor -> scissor wins
'''
while True:
    ccount = 0
    ucount = 0 


    uc = int(input('''
    Game start......
    1 Yes
    2 No | Exit'''))
    if uc==1:
        for a in range(1,6):
            userInput= int(input('''
1. Rock 
2. Paper
3. Scissor                      
            '''))
            if userInput==1:
                uchoice="rock"
            elif userInput==2:
                uchoice="paper"
            elif userInput==3:
                uchoice="scissor"
            cchoice = random.choice(l)
            if cchoice ==uchoice:
                print("Computer Value ---", cchoice)
                print("User Value ---",cchoice)
                print("Game Draw...👎")
                ucount = ucount +1
                ccount = ccount+1 

            elif (uchoice =="rock" and cchoice =="scissor" ) or (uchoice 
                =="paper" and cchoice=="rock") or (uchoice =="scissor" and cchoice == "paper"):
                 print ("You Win !...🤴")
                 ucount = ucount+1


            else:

                print("Computer Value ---", cchoice)
                print("User Value ---",uchoice)
                print("Computer Win !...")
                ccount = ccount+1    

        if  ucount == ccount:
            print("Final Game Draw.... ")  
            print("User Score --- ", ucount)  
            print("Computer Score --- ",ccount)
        elif ucount > ccount: 
            print("Final Computer Win The Game.... ")  
            print("User Score --- ", ucount)  
            print("Computer Score --- ",ccount)             
        else:
            print("Final Computer Win The Game.... ")  
            print("User Score --- ", ucount)  
            print("Computer Score --- ",ccount) 


    else:
        break
       



            
