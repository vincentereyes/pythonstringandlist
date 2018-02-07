x = [4,"Tom",1,"Michael",5,7,"Jimmy Smith"]

def drawstars(arr):
	for i in range(0, len(arr)):
		stars = ""
		if isinstance(arr[i], int):
			for i in range(0,arr[i]):
				stars += "*"
		else:
			for x in range(0, len(arr[i])):
				stars += arr[i][0]
		print stars.lower()
drawstars(x)