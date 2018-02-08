class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	def displayInfo(self):
		print self.price
		print self.max_speed
		print self.miles
	def ride(self):
		self.miles += 10
		print "Riding"
		return self
	def reverse(self):
		print "Reversing"
		if self.miles == 0:
			pass
		else: 
			self.miles -= 5
		return self
		

roadbike = Bike(3000, "40mph")
mountainbike = Bike(2400, "20mph")
bmxbike = Bike(300, "10mph")

roadbike.ride().ride().ride().reverse().displayInfo()
mountainbike.ride().ride().reverse().reverse().displayInfo()
bmxbike.reverse().reverse().reverse().displayInfo()
