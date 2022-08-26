password=9915
count=0
while True:
    ramz=int(input("enter your password: "))
    a=int(ramz/1000)
    if (0<a<=9):
        count+=1
        if ramz==9915:
            print("warning! we will call to the police officer!")
            break
        elif ramz==password:
            print("your password is True.")
            break
        elif ramz<3:
            print("wrong! please try agaim later!")
        elif ramz==3:
            print("you can not continue.")
            break
        else:
            print(" please try agagin!")