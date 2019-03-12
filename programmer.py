class Programmer():
	hobby = 'play computer'
	def __init__(self,name,age,weight):
		self.name = name
		self._age = age
		self.__weight = weight

	def get_weight(self):
		return self.__weight

	def __eq__(self,other):
		if isinstance(other,Programmer):
			if(self._age == other._age):
				print('same age')
			else:
				print('different age')
		else:
			print('We need you to input a programmer')
#############################################################
	def __getattribute__(self,name):						#
		return super().__getattribute__(name);				#
#############################################################


class BackendProgrammer(Programmer):
	def __init__(self,name,age,weight,language):
		super().__init__(name,age,weight)
		self.language = language

if __name__ == '__main__':
	jjj  = BackendProgrammer('jjj',24,120,'Python')
	momo = Programmer('momo',25,100)
	jjj == momo
	print(dir(jjj))
	print(jjj.__dict__)
	print(jjj.get_weight())
	print(type(jjj))
	print( isinstance(jjj,Programmer))
	print(jjj._age)
