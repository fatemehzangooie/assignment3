password=9915
i=0
while True:
    ramz=int(input("enter your password: "))
    
    if 1000<=ramz<=9999:
        i=i+1
        if ramz==5199:
            print("warning! we will call to the police officer!")
            break
        elif ramz==password:
            print("your password is True.")
            break
        elif i<3:
            print("wrong! please try agaim later!")
        elif i==3:
            print("you can not continue.")
            break
        else:
            print(" please try agagin!")