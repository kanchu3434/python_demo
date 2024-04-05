import re
s = 'https://www.amazon.in/software-engeenering----/dp/0071240837'
obj1=re.findall('\w+://',s)
print(obj1)
obj2 = re.findall('://([w_\.]+)',s)
print(obj2)
obj3 = re.findall('://([\w\_\.]+)(:(\d+))?',s)
print(obj3)
