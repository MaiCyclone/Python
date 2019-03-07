def build_person(first_name,last_name,age = ''):
	person = {'first_name' : first_name, 'last_name' : last_name}
	if age:
		person['age'] = age
	return person

jjj1 = build_person('Yuxuan','Jiang')
print(jjj1)
jjj2 = build_person('Yuxuan','Jiang',28)
print(jjj2)
