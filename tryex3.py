try :
    th=open("testfile.txt","w")
    try :
        th.write("this is trial file")
    finally :
        print("going to close file")
        th.close()
except IOError :
        print("error can't find the file or write data")
