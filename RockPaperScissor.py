import random
user=int(input("enter your choice(0 for rock,1 for paper,2 for scissor):"))
comp=random.randint(0,2)
print("computer choice:",comp)
if(comp==user):
    print("draw")
    elif(user==0 and comp==2):
        print("you win")
    elif(user==1 and comp==0):
        print("you win")
    elif(user==2 and comp==1):
        print("you win")
    else:
        print("not suitable")
