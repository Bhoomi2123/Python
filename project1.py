# Creating a mini calculator that performs 6 operations (+, -, *, **, /, %) on 2 numbers

first = input("Enter first number : ")
second = input("Enter second number : ")

operation = input("Enter the number of operator : ")
# 1: +, 2: -, 3: *, 4: **, 5: /, 6: %

if operation == "1" :
    result = int(first) + int(second)
elif operation == "2" :
    result = int(first) - int(second)
elif operation == "3" :
    result = int(first)  * int(second)
elif operation == "4" :
    result = int(first)  ** int(second)
elif operation == "5" :
    result = int(first)  / int(second)
elif operation == "6" :
    result = int(first)  % int(second)
else:
    print("Invalid operation!!")
    
print(result)
    

