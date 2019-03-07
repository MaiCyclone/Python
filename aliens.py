aliens = []
for item in range(30):
	item = {'colar':'green','speed':'slow','points':5}
	aliens.append(item)
	
for  item in aliens[:5]:
	print(item)
	
print("...")

print("Threr are " +str(len(aliens)) +" aliens in total")

for item in aliens[:3]:
	item['color'] = 'yellow'
	item['speed'] = 'medium'
	item['points'] = 10
	
for  item in aliens[:5]:
	print(item)
