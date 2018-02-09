class Animal(object):
	"""docstring for Animal"""
	def __init__(self, name, health):
		self.name = name
		self.health = health
	def walk(self):
		self.health -=1
		return self
	def run(self):
		self.health -=5
		return self
	def displayhealth(self):
		print self.health
class Dog(Animal):
	"""docstring for Dog"""
	def __init__(self, name):
		super(Dog, self).__init__(name, 150)
	def pet(self):
		self.health +=5
		return self
class Dragon(Animal):
	"""docstring for Dragon"""
	def __init__(self, name):
		super(Dragon, self).__init__(name, 170)
	def fly(self):
		self.health -= 10
		return self
	def display(self):
		self.displayhealth()
		print "I am a Dragon"
