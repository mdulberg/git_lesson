
writeMe= 'Example text'

'''openning file for writing (will over-write the contents)'''
saveFile = open('exampleWrite.txt','w')
'''writing to the file'''
saveFile.write(writeMe)
saveFile.write('\n')
'''closing and saving the file'''
saveFile.close()

appendMe= 'more text'
saveFile = open('exampleWrite.txt','a')
saveFile.write(appendMe)
saveFile.write('\n')
saveFile.write(appendMe)
saveFile.write('\n')
saveFile.close()


'''  Reading from the file above  '''

readMe = open('exampleWrite.txt','r').read()
print(readMe)

'''  Reading a file and splitting it by new line  \n '''
'''  This takes each line and puts it into a list as an entry '''
print('\n\n\n')
splitMe = readMe.split('\n')
print(splitMe)
''' printing the second item from the list'''
print('\n\n\n')
print(splitMe[2])


