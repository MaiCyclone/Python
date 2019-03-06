def person(last,first,**info):
	profile = {}
	profile['last_name'] = last
	profile['first_name'] = first
	
	for key, value in info.items():
		profile[key] = value
	return profile


#jjj = person('Jiang','Yuxuan',location = 'Ottawa',hobby = 'eat')
#print(jjj)
