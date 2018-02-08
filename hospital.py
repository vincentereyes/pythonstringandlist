class Patient(object):
	"""docstring for Patient"""
	def __init__(self, idnum, name, aller, bednum):
		self.idnum = idnum
		self.name = name
		self.aller = aller
		self.bednum = bednum
class Hospital(object):
	"""docstring for Hospital"""
	def __init__(self, name, capacity):
		self.name = name
		self.capacity = capacity
		self.records = []
		self.patients = []

	def admit(self, x):
		if len(self.patients) == self.capacity:
			print "Hospital is Full"
		else:
			self.patients.append(x)
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

a = Patient(1, "bryant", "shrimp", 1)
b = Patient(2, "bryant", "shrimp", 2)
c = Patient(3, "yaboi", "shrimp", 3)
f = Patient(4, "bryant", "shrimp", 4)
d = Hospital("hey", 3)
d.admit(a).admit(b).admit(c).admit(f)
d.discharge(5)