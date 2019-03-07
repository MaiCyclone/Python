class Dog():
	def __init__(self,age,name):
		self.name = name
		self.age = age
	def sit(self):
		print(self.name + " is sitting")
	def roll(self):
		print("roll")

wangwang = Dog(1,'wangwang')
wangwang.sit()
wangwang.roll()
