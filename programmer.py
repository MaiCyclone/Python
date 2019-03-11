class Programmer():
	hobby = 'play computer'
	def __init__(self,name,age,weight):
		self.name = name
		self._age = age
		self.__weight = weight
		
	def get_weight(self):
		return self.__weight
		
		
class BackendProgrammer(Programmer):
	def __init__(self,name,age,weight,language):
		super().__init__(name,age,weight)
		self.language = language

if __name__ == '__main__':
	jjj  = BackendProgrammer('jjj',24,120,'Python')
	print(dir(jjj))
	print(jjj.__dict__)
	print(jjj.get_weight())
	print(type(jjj))
	print( isinstance(jjj,Programmer))
	
