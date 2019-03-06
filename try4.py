#for item in range(1,1000000):
#	print(item)

#milionList = [item for item in range(1,1000001)]
#print(milionList[-10:])
#print(min(milionList))
#print(max(milionList))
#print(sum(milionList))

#odd = [item for item in range(1,21,2)]
#print(odd)

#three = [item for item in range(3,31,3)]
#print(three)

#cube = [item**3 for item in range(1,11)]
#print(cube)

tmp = ['666','777','888','999','000','111','222','333']
copy_tmp = tmp[:]

tmp.append('jjj')
copy_tmp.append('momo')
print(tmp)

for item in tmp:
	print(item)
print(copy_tmp)
for item in copy_tmp:
	print(item)


tp = ('egg','chicken','beef','lamb','coke')
for item in tp:
	print(item)

