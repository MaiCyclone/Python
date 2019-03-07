friends = ['jay','john','peter','eric']
print(friends)
friends[0] = 'jjj'
print(friends)
friends.append('momo')
print(friends)
friends.insert(0,'Dad and Mom')
friends.insert(2,'zed')
print(friends)

print('\nsry ' + friends.pop() + ' table is full')
print(friends)
print('\nsry ' + friends.pop() + ' table is full')
print(friends)
print('\nsry ' + friends.pop() + ' table is full')
print(friends)
print('\nsry ' + friends.pop() + ' table is full')
print(friends)
print('\nsry ' + friends.pop() + ' table is full')
print(friends)

del friends[-1]
print(friends)
del friends[-1]
print(friends)
