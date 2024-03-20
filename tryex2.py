try :
    f = open("trial.txt")
    f.write("welcome to mca")
except:
    print("something went wrong while writting the file")
finally:
    f.close()