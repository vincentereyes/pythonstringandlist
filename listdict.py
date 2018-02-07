name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(list1, list2):
  new_dict = {}
  fave = []
  
  if len(list1) > len(list2):
  	fave = zip(list1, list2)
  elif len(list1) < len(list2):
  	fave = zip(list2, list1)
  else:
  	fave = zip(list1, list2)
  new_dict = dict(fave)
  return new_dict
print make_dict(name, favorite_animal)