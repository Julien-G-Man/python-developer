i = 0
while i < 10: #== int(i):
    print(i)
    i += 1 
print(type(i))   

mylist = ['a', 'b', 'c'] 
for x in range(5):
    print(x)
    
for y in range(3, 5):
    print(y)  

for z in mylist:
    print(z)
    if z == 'b':
        break
    print(z)

mydict = {
    'name': 'James',
    'age': 20,
}
for a in mydict:
    print(f"{a}: {mydict[a]}")