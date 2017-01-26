
x = 3
y = 7
z = 10
'''
if x>y:
	print(x,'is greater than',y)
elif x>z:
	print(x,'is greater than',z)
elif y>z:
	print(y,'is greater than',z)
else:
	print('nothing was the case')
'''

'''
if x>y:
        print(x,'is greater than',y)
elif x<z:
        print(x,'is less than',z)
elif y<z:
        print(y,'is less than',z)
else:
        print('nothing was the case')

'''
'''
if x>y or x<z:
        print('one of the statements is true')
elif x<z:
        print(x,'is less than',z)
elif y<z:
        print(y,'is less than',z)
else:
        print('nothing was the case')
'''

if x<y and x<z:
        print('both statements must be true')
elif x<z:
        print(x,'is less than',z)
elif y<z:
        print(y,'is less than',z)
else:
        print('nothing was the case')



