import random
num1=0
num2=99
number=random.randint(num1,num2)
while True:
    print("is it" ,number,"yes or not?!")
    x=input()
    if x=="yes" :
        print("you win.")
        break
    elif x=="not":
        result=input("it is bigger or smaller= ")
        if result=="bigger":
            num1=number+1
            number=random.randint(num1,num2)
        elif result=="smaller":
            num2=number-1
            number=random.randint(num1,num2)
        else:
            print("your ansewr bigger or smaller!")
            continue
        
    else:
            print("your answer correct or incorrsct")
            continue