class Patient(object):
	"""docstring for Patient"""
	def __init__(self, idnum, name, aller):
		self.idnum = idnum
		self.name = name
		self.aller = aller
		self.bednum = 0
class Hospital(object):
	"""docstring for Hospital"""
	def __init__(self, name, capacity):
		self.name = name
		self.capacity = capacity
		self.records = []
		self.patients = []

	def admit(self, x, y):
		if len(self.patients) == self.capacity:
			print "Hospital is Full"
		else:
			self.patients.append(x)
			x.bednum = y
			print "Admission is complete"
		return self
	def discharge(self, y):
		counter = 0
		for i in range(0, len(self.patients)):
			if y == self.patients[i].idnum:
				self.patients[i].bednum = 0
				self.records.append(self.patients.pop(i))
				counter += 1
		if counter == 0:
			print "Patient not found"

a = Patient(1, "bryant", "shrimp")
b = Patient(2, "bryant", "shrimp")
c = Patient(3, "yaboi", "shrimp",)
f = Patient(4, "bryant", "shrimp")
d = Hospital("hey", 3)
d.admit(a).admit(b).admit(c).admit(f)
d.discharge(5)