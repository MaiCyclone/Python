class Car():
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.meter = 0;
	def get_info(self):
		print('The car is '+self.make+' '+self.model + ' build in ' + str(self.year))
	def get_meter(self):
		print(self.meter)
	def update_meter(self,meter):
		if(meter > self.meter):
			self.meter = meter
		else:
			print('invalid action')
	def inc_meter(self,meter):
		self.meter = self.meter + meter

#audi = Car('audi','a4',2011)
#audi.get_info()
#print('current meter')
#audi.get_meter()

#audi.update_meter(10000)
#print('after update 10000')
#audi.get_meter()
#print('after update 500')
#audi.update_meter(500)



