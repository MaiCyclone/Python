favourite_languages = {
	'Jjj' : ['Python','JAVA'],
	'Momo' : ['Python','Java'],
	'Jackey' :[ 'C++','C'],
	'Roy' : ['JavaScript','ruby']
}

favourite_languages['Tuhao'] = ['C++']

friends = ['jjj','momo','roy']

#for name in favourite_languages:
#	print(name)
#	if name.lower() in friends:
#		
#		print('Hi ' + name + ' Your favourite languages is ' +
#		favourite_languages[name])


#for language in set(favourite_languages.values()):
#	print(language)

for name, lang in favourite_languages.items():
	print("\n"+name+"'s favoutite languages are")
	for item in lang:
		print(item)
