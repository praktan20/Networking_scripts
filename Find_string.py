import re
def find_string(input):
	if len(input) !=0:
		a = re.findall(r'Host: ' + '.*', input)
		b = re.findall(r'Cost: ' + '.*', input)
		for i,j in zip(a,b):
			c = i.strip('Host: ')
			d = j.strip('Cost: ')
			print d + ',' + c		
	else:
		return False		
my_string = '''Host: abc.amazon.com
Cost: 20
EOR
Host: def.amazon.com
Cost: 5
EOR
Host: ghi.amazon.com
Cost: 9
EOR
Host: foo.amazon.com
Cost: 4
EOR
Host: bar.amazon.com
Cost: 7
EOR'''
print find_string(my_string)