type1=int(input("select: hr to sec=1 and sec to hr=2: "))
if type1==1:
    while True:
     hour=int(input('enter hours: '))
     min=int(input("enter minute: "))
     sec=int(input("enter seconed: "))
     if (hour<24) and (min<60) and (sec<60):
         hour=hour*3600
         min=min*60
         sum=hour+min+sec
         print(sum,"sec: ")
         break
     else:
         print("enter your number: ")
         continue
elif type1==2:
    while True:
        sec=int(input("enter clock: "))
        if sec<=86400:
            min=int(sec/60)
            if min >=60:
                hour=int(min/60)
                a1=int(min%60)
                b1=int(sec%60)
                print("hour: ",hour,"minute: ",a1,"seconed: ",b1)
                break
            else:
                print("try again!")
                continue
         
   