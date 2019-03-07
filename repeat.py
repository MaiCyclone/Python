#msg = '';
#while msg != 'quit':
#	msg = input("I can repeat what you say: ")
#	if(msg != 'quit'):
#		print(msg)



#tmp = input('give me a number: ')
#num = int(tmp)
#if(num % 10 == 0):
#	print('it is multiple of 10')
#else:
#	print('i need a number which is multiple of 10')

active = True
msg = ''
while active :
	if(msg == 'quit'):
		active = False;
	else:
		msg = input("I'll repeat: ")
		if(msg != 'quit'):
			print(msg)
