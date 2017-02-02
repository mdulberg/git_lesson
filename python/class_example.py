

''' a calss is an aggrigation of functions '''
class calc:
	def add(x,y):
		answer = x+y
		print(answer)
	def sub(x,y):
		answer = x-y
		print(answer)
	def mult(x,y):
		answer = x*y
		print(answer)
	def div(x,y):
		answer = x/y
		print(answer)
	def add3(x,y,z):
		answer = x+y+z
		print(answer)

''' you can call a function from a class by using  class.function(function inputs) '''

x = calc.add(3,4)
print(x)

y = calc.div(3,4)
print(y)

print(calc.mult(3,4))

print(calc.add3(5,6,7))






