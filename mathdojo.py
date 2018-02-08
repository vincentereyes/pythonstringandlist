class MathDojo(object):
	"""docstring for MathDojo"""
	def __init__(self, temp):
		self.temp = temp

	def add(self, *num):
		for i in num:
			if type(i) == tuple or type(i) == list:
				for j in i:
					self.temp += j	
			else:
				self.temp +=i
		return self

	def sub(self, *num):
		for i in num:
			if type(i) == tuple or type(i) == list:
				for j in i:
					self.temp -= j	
			else:
				self.temp -=i
		return self

	def result(self):
		print self.temp

md = MathDojo(0)
md.add(2).add(2,5).sub(3,2).result()
md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).sub(2, [2,3], [1.1,2.3]).result()
	
		