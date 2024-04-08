import re
txt = "Iam student of MCA"
x = re.findall("\w",txt)
print(x)
if x:
    print("yes, there is at least one match")
else:
    print("no match")