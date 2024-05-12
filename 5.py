list = [1,2,3,2,1]
# list = [1,2,3,1]

copy = list.copy()
copy.reverse()

if(copy == list):
    print("Palindrome !")
else:
    print("Not Palindrome !")