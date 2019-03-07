class Restaurant():
	def __init__(self,name,food_type):
		self.name = name
		self.food_type = food_type
	def describe(self):
		print(self.name + " servers " + self.food_type)



mand = Restaurant("Mandarin","buffet")
mand.describe()
