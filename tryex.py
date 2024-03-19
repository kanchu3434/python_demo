try :
    print(x)
except NameError:
    print("variable is not define")
except :
    print("something is wrong") 
finally :
    print("the try except is finished")     