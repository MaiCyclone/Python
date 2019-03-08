from car import Car

class Electric_Car(Car):
	def __init__(self,make,model,year):
		super().__init__(make,model,year)

class Battery():
	def __init__(self,size = 70):
		self.size = size
	
	def get_range(self):
		if self.size == 70:
			print('It can ran 240 mile')
		else:
			
			print("It can ran 320 mile")
