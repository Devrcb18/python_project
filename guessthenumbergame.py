import random
class guess:
    def play(self,u):
        self.name=u
        b=random.randint(1,100)
        t=0
        print("GUESS THE NUMBER GAME".center(40,"-"))
        while True: 
            t += 1
            try:
                n = int(input("Make a guess: "))
                self.num = n

                if n > b:
                    print("Your guess is high!".title())
                elif n < b:
                    print("Your guess is low!".title())
                else:
                    print("Perfect Guess!".title())
                    break 
            except ValueError:
                print("Please enter a valid number.".title())

        with open("scorebook.txt","a") as f1:
           f1.write(f"{self.name} your score is: {t}\n".title())
                    
def scoreshow():
    with open("scorebook.txt","r") as y:
        for i in (y.readlines()):
             print(i)
        print("thankyou for playing".center(30,"-"))
def clearscore():
    try:
        with open("scorebook.txt", "w") as f:
            f.truncate(0) 
        print("All previous scores have been deleted.".title())
    except FileNotFoundError:
        print("No score file found to delete.".title())
p1=guess()
p2=guess() 
name1=input("player:1--")
name2=input("player:2--")
while True:
    o=int(input("Enter your choice:\n1) Player 1 to play\n2) Player 2 to play\n3) Show the scorecard\n4) Clear all scores\n5) Exit\n".title())) 
    if(o==1):
     p1.play(name1)
    elif(o==2):
     p2.play(name2) 
    elif(o==3):
     scoreshow()   
    elif o==4:
        clearscore()
    elif o==5:
        print("Exiting the game. Goodbye!".title())
        break
    else:
        print("Invalid choice. Please choose a valid option.".title())