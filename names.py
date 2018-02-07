users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def display(g):
	for key,data in g.items():
		print key
		count = 1
    		for value in data:
    			print str(count) + " - " + value['first_name'] + " " + value['last_name'] + " - " + str(len(value['first_name'] + value['last_name']))
    			count += 1
display(users)