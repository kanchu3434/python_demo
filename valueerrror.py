try :
    num=int(input("enter any number"))
    if(num<=0):
        raise ValueError("you have entered negative number")
except ValueError as e :
    print(e)    