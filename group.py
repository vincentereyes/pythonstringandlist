'''
a = "I love to code"
b = ""
print a.capitalize()
print a.upper()
print a.lower()
print a.count('o')
print a.find('l')
print a.index('e')

e,f,g,h = a.split(" ")
print e
print f
print g
print h

print b.join(a)

print a.replace("code", "pingpong")

print("I love {} code".format("aaa"))
'''

a = [3,1,6,8,5,2,8, "hello"]
print len(a)
print max(a)
print min(a)
print a.index(5)
a.append(6)
a.pop()
a.remove("hello")
a.insert(0, "insert")
a.insert(4, False)
a.sort()
print a
a.reverse()
print a
a.extend([5,4])
print a
a.sort()
print a