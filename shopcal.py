#WAP WHICH WILL KEEP ADDDING THE NOS .PRESS Q TO STOP.


sum=0
while(True):
    userinput = input("enter the item price or press q to escape ")
    if(userinput!='q'):
        sum=sum + int(userinput)
        print(f"your bill so far{sum}")
    else:
        print(f"ypur total bill is {sum}. Thanks for shopping with us.")
        break
