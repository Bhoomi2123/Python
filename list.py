marks = [90,80,70]
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[-1])
print(marks[-2])
print(marks[-3])

print(marks[0:2])   # 2 not included, appends at last

for i in marks:
    print(i)
    
marks.append(99)
print(marks)

marks.insert(1,91)   #insert at given index
print(marks)

print(99 in marks)

print(len(marks))

i=0
while i < len(marks):
    print(marks[i])
    i+=1
    
marks.clear()
print(marks)