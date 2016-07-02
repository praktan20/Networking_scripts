input= '''Host: abc.amazon.com
Count: 4
EOR
Host: def.amazon.com
Count: 5
EOR
Host: foo.amazon.com
Count: 10
EOR
Host: bar.amazon.com
Count: 1
EOR
..
..
..'''

import re
a = re.findall(r"Host: " + r'(.*)', Input)
b = re.findall(r"Cost: " + r'(.*)', Input)
for i,j in zip(a,b):
    c = i.strip('Host: ')
    d = j.strip('Cost: ')
    print d +','+ c
################# 
#output##
#4,abc.amazon.com
#5,def.amazon.com
#10,foo.amazon.com
#1,bar.amazon.com

