jjj = {
'first_name' : 'Yuxuan',
'last_name' : 'Jiang',
'age' : '24',
'city' : 'Toronto'
}

print(jjj['first_name'])
print(jjj['last_name'])
print(jjj['age'])
print(jjj['city'])

f_num = {
	'jjj' : 7,
	'momo' : 6,
	'Mom' : 8,
	'Dad' : 10
}

print("jjj's favourite number is " + str(f_num['jjj']))

for key,value in jjj.items():
	print('\nKey: ' + key,
		',Value: ' + value)

for key in jjj.keys():
	print(key.title())
	
for name in f_num:
	print(name)
