#List Methods
names1 = [2, 5, 3 , 8, 1]
names2 = ['1Janet', 'Charlot', 'Julien', 'Jack']

# iterating over two lists at once
for n, a in zip(names1, names2):
   print(n, a)

names3 = names2.copy()
names2.remove('Julien')
del names2[-2]

#names2.insert(1, 'Charles')
#print(len(names[0]))
#names[1] = 'James'
#print(type(names[1]))
names1.sort()
names2.sort()
names1.reverse()
#print(names1.extend(names2))
print(names2)
print(names1)
#print(names2.count())
print(names3)