# int

s = "100"

c = int(s,2)
print("String converted to int base 2: ", c)

c = int(s)
print("String converted to int base 10: ", c)

# str

print("int => string: ", str(10))
print("float => string: ", str(10.0))
print("complex => string: ", str(10 + 2939j))

# list

print("string => list: ", list('Alexis'))
print("int => list: ", list(str(12)))
print("tuple => list: ", list(tuple('Alexis')))

# set

print("string => set: ", set('Alexis'))
print("int => set: ", set(str(12)))
print("tuple => set: ", set(tuple('Alexis')))
