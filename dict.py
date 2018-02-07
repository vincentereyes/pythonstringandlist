info = {"Name": "Vince", "Age": "24", "Blace": "United States", "Lang": "Python"}

def displayinfo(a):
	print "My name is " + a["Name"]
	print "My age is " + a["Age"]
	print "My country of birth is " + a["Blace"]
	print "My favorite language is " + a["Lang"]
displayinfo(info)