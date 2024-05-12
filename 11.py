def sums(n):
    if(n == 0):
        return 0
    s = sums(n-1) + n
    return s

num = int(input("Enter number : "))
print(sums(num))