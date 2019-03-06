def PrintCase(current,target):
	while current:
		tmp = current.pop()
		print("printing " + tmp)
		target.append(tmp)
		print("printing "+tmp+" done")

def ShowAllCase(items):
	for item in items:
		print(item + " has been add to the warehouse")


case = ['iphone case',"huawei case",'meizu case']
finished = []

print(case)
PrintCase(case[:],finished)
ShowAllCase(finished)
print(finished)
print(case)
