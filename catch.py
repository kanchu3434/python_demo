def extrial(a,b):
    try :
        c=(a+b)/(a-b)
    except ZeroDivisionError :
        print("a/b result is 0")
    else :
        print(c)
