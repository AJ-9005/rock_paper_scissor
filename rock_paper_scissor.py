import random
def home():
    x=False
    while x==False:
        choice=int(input("Start game?\n1. Yes\n2. No\n "))
        if choice==1:
            playgame()
        elif choice==2:
            x=True
        else:
            print("\nPlease enter valid choice!")
def choice(y,z):
    if y==1:
        print("You chose stone")
    elif y==2:
        print("You chose paper")
    elif y==3:
        print("You chose scissor")
    if z==1:
        print("Computer chose stone")
    elif z==2:
        print("Computer chose paper")
    elif z==3:
        print("Computer chose scissor")
def playgame():
    yp=0
    cp=0
    print(f"Your points:{yp}\nComputer points:{cp}")
    while yp<5 and cp<5:
        cc=random.randint(1,3)
        yc=int(input("\nEnter your choice: \n1.Stone \n2.Paper \n3.Scissor \n"))
        if (yc==1 and cc==1) or (yc==2 and cc==2) or (yc==3 and cc==3):
            choice(yc,cc)
            print("Draw!")
        elif (yc==1 and cc==2) or (yc==2 and cc==3) or (yc==3 and cc==1):
            choice(yc,cc)
            print("Computer won!")
            cp+=1
        elif (yc==1 and cc==3) or (yc==2 and cc==1) or (yc==3 and cc==2):
            choice(yc,cc)
            print("You won!")
            yp+=1
        else:
            print("Please enter valid choice!")
    if yp==5:
        print("You won the game!")
    else:
        print("Computer won the game!")
home()