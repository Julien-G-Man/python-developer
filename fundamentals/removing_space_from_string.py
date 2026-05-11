text = "a b c d"
clean = text.replace(" ",  "")
print(clean)

# can also be used generally to replace a character or group of characters with another
name = "Eric Monger"
new = name.replace("Eric", "Bruce").replace("Monger", "Wayne")
print(name)
print(new)