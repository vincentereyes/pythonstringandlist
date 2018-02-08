class Car(object):
	"""docstring for Car"""
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		self.tax = 0
		if price > 10000:
			self.tax = 0.15
		else:
			self.tax = 0.12
		self.display_all()
	def display_all(self):
		print "Price: " + str(self.price)
		print "Speed: " + self.speed
		print "Fuel: " + self.fuel
		print "Mileage: " + self.mileage
		print "Tax: " + str(self.tax)

honda = Car(4500, "100mph", "Full", "30mpg")
bmw = Car(12000, "300kph", "Half", "27mpg")
hyundai = Car(8000, "60mph", "Almost full", "34mpg")
audi = Car(11000, "200mph", "Empty", "23mpg")
toyota = Car(2000, "50mph", "Full", "40mpg")
dodge = Car(3000, "50mph", "Above Empty", "2mpg")
