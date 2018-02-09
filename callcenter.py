class Call(object):
	"""docstring for Call"""
	def __init__(self, id1, cname, cpnum, time, reason):
		self.id1 = id1
		self.cname = cname
		self.cpnum = cpnum
		self.time = time
		self.reason = reason
	def display(self):
		print self.id1
		print self.cname
		print self.cpnum
		print self.time
		print self.reason

class CallCenter(object):
	"""docstring for CallCenter"""
	def __init__(self):
		self.calls = []
		self.queue = 0
	def add(self, x):
		self.calls.append(x)
		self.queue = len(self.calls)
		return self
	def info(self):
		for i in self.calls:
			print i.cname
			print i.cpnum
		print self.queue
	def remove(self):
		self.calls.pop(0)
		self.queue = len(self.calls)
		return self


boomin = CallCenter()
a = Call(12, "vince", "5109876543", 23, "dunno")
b = Call(13, "john", "782364872", 23, "dumb")
boomin.add(a)
boomin.add(b)
boomin.info()
boomin.remove()
boomin.info()