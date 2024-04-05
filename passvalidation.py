import re
def main():
 password = 'kanchan123@'
 reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,8}"
 pat= re.compile(reg)
 mat = re.search(pat,password)
 if mat:
    print("password is valid")
 else:
    print("Invalid password")
 if __name__ =='__main__':
   main()

