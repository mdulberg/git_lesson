#

x = 6
'''
def example():
	z = 5
	print(z)
example()
#can not do the following line:
#print(z)

def example2():
	z = 4
	print(z)
	print(x)
example2()

# cano't do the following since a global variable cannot be changed
def example3():
	z = 4
	print(z)
	x += 1
	print(x)
example3()

# so instead assign it to another variable:

def example4():
        z = 4
        print(z)
        y = x + 1
        print(y)
example4()
'''

def example5():
	z = 4
	print(z)
	y = x + 1
	print(y)
	return y
example5()
x = example5()
print('new x is',x)

