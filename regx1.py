import re
txt ="the orange in in indi comes from nagpur"
x = re.findall("ora*",txt)
if x:
    print("yes, there is at least one match")
else:
    print("no match")