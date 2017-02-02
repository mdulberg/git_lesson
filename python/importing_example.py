
'''  a few ways to import. this is one way'''
'''
import statistics

exList = [4,5,6,2,9,8,9,9,11,15,222]

print(statistics.mean(exList))
'''
''' another way'''
'''
import statistics as s

exList = [4,5,6,2,9,8,9,9,11,15,222]

print(s.mean(exList))
'''

''' importing only one function from a class'''
'''
from statistics import mean 

exList = [4,5,6,2,9,8,9,9,11,15,222]

print(mean(exList))
'''

''' importing two functions'''
from statistics import mean, stdev

exList = [4,5,6,2,9,8,9,9,11,15,222]

print(mean(exList))
print(stdev(exList))

''' importing all function, but without having to use class.function syntax, use:'''
from statistics import *



