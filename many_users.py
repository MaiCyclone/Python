users = {
'aeinstein': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton',
},
'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris',
},
}

for name,info in users.items():
	print('\nusername is ' + name)
	print('name: ' + info['first'] +" " + info['last'] )
