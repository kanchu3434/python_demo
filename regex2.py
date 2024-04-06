# import library
import re
txt ="there are mny historical palces around Ahemednagar"
# use regular expression +:one or more occurance
x = re.findall("re+",txt)
print(x)
if x:
    print("yes, there is at least one match")
else:
    print("no match")