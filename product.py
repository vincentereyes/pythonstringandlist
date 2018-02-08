class Product(object):
	"""docstring for Product"""
	def __init__(self, Price, ItemName, Weight, Brand):
		super(Product, self).__init__()
		self.Price = Price
		self.ItemName = ItemName
		self.Weight = Weight
		self.Brand = Brand
		self.Status = "for sale"
	def sell(self):
		self.Status = "sold"
		return self
	def addTax(self, tax):
		finalprice = self.Price + (self.Price * tax)
		return finalprice
	def returns(self, reason):
		if reason == "defective":
			self.Status = "Defective"
			self.Price = 0
		elif reason == "opened":
			self.Status = "Used"
			self.Price -= (self.Price * .20)
		elif reason == "sealedbox":
			self.Status = "for sale"
		return self
	def display(self):
		print self.Price
		print self.ItemName
		print self.Weight
		print self.Brand
		print self.Status

food = Product(50, "noodles", "50grams", "spicynoodlechallenge")
food.display()
print food.addTax(.10)
food.returns("opened").display()