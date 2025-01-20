import random
import emoji
def victory(num,b):
    if(num==b):#tie
        return 1
    elif(((num==1)and (b==-1)) or((num==-1)and (b==0))or((num==0)and (b==1))):#win
        return 2
    elif((num==1 and b==0)or(num==-1 and b==1) or(num==0 and b==-1)):#lost
        return 3

print("---SCISSOR PAPER ROCK!---")
dict={1:":scissors:",-1:":page_facing_up:",0:":rock:"}
while(True):
    n=int(input("enter choices(-1,0,1) for respectively scissor paper and rock---".title()))
    b=random.randint(-1,1)
    if(n in range(-1,2)): 
     print("you selected----",emoji.emojize(dict[n]))  
     print("comp selected---",emoji.emojize(dict[b]))
     o=victory(n,b)
     if(o==2):
        print("You Won!")
        break
     elif(o==3):
        print("You Lost!")    
        break
     elif(o==1):
        print("Match tie...Retry!") 
    else:
        print("invalid")       
