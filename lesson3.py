# while #condition :
#     #run this line untill condition is true
#     print()


x1 = int(input("Enter x1: "))
x2 = int(input("Enter x2: "))
 
 
x = x1 + 1
 
sum = 0
 
while x < x2:
    sum = sum + x
    x += 1
    print(f"sum: {sum}")
print("The sum of all integers between", x1, "and", x2, "is", sum)
