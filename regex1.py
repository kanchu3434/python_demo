import re
txt ="the orange in in indi comes from nagpur"
# use regular expression *-zero or more occurance
x = re.findall("ora*",txt)
if x:
    print("yes, there is at least one match")
else:
    print("no match")