def website(font,bg_color,font_size,font_color):
	print('font is :',font)
	print('background color is :',bg_color)
	print('font size is :',font_size)
	print('font_color is :',font_color)

website('TNR','white','11','black')
#order must be kept in the way above. 
#if we don't want to keep the order we can explicitly say what's the value of each

website(bg_color='white',font_color='black',font_size='11',font='TNR')


# a function can have defaults:

def website2(font='TNR',bg_color='white',font_size='11',font_color='black'):
	print('font is :',font)
	print('background color is :',bg_color)
	print('font size is :',font_size)
	print('font_color is :',font_color)

website2(font='not TNR at all')

