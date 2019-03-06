alien_color = 'gre'

if(alien_color == 'green'):
	print('5 points!')
elif(alien_color == 'yellow'):
	print('10 points!')
else:
	print('15 points!')
	
age = 12
if(age < 2):
	print('baby')
elif(age > 2 and age < 4):
	print('toddler')

#usernames = ['admin','zxc','jyx','dym','yuiyui']
usernames = []
if usernames:
	for item in usernames:
		if(item == 'admin'):
			print('report?')
		else:
			print('hello ' + item + ' welcome back')
else:
	print('we need some users')


current_users = ['admin','zxc','jyx','dym','yuiyui']
new_users = ['admin','JYX','yui','tyu','momo']

for item in new_users:
	if item.lower() not in current_users:
		print( item + ' is a valid user name')
	else:
		print(item + ' is not avalidble. please choose another user name')
