import random
sum=0
while True:
    tas=random.randint(1,6)
    if tas==6:
        print(tas)
        print("done!")
        sum+=tas
        continue
    else:
        sum+=tas
        print(tas)
        print("sum: ",sum)
        if tas<6:
            break
        else:
            continue