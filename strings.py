name="Tony stark"

print(name.upper())
print(name.find('s'))
print(name.find('S'))  # returns index & if not found, returns -1

print(name.replace("Tony stark", "Ironman"))    # does not change original string
print(name)

print('T' in name)   # find if it is present