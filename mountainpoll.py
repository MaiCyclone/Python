active = True
result = {}

while active:
	name = input('Please enter ytour name: ')
	mountain = input('You climb which mountain: ')
	result[name] = mountain
	condition = input("add another? Y/N")
	if(condition.lower() == "n"):
		active = False


for name,mountain in result.items():
	print(name + " climbs " + mountain)
