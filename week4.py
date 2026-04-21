# # The user types in two numbers.
# # Print all the numbers in the specified range.

# #1

start = int(input("start :"))
end = int(input("end :"))
 
for i in range(start, end):
    print(i)

# #2

start = int(input("start :"))
end = int(input("end :"))

data = range(start, end)

for i in data:
    if i % 2 != 0:
        print(i)

# #3

# # The user types in two numbers.
# #  Print all odd numbers in the specified range.
 
start = int(input("start :"))
end = int(input("end :"))
 
data = range(start, end)
 
for i in data:
    if i % 2 == 1 :
        print(i)
 

#4

start = int(input("start :"))
end = int(input("end :"))

data = range(start, end)

for i in data:
    if i % 2 == 0:
        print(i)


# The user types in two numbers.
# Print all numbers in the specified range in descending order.
 
start = int(input("start :"))
end = int(input("end :"))
 
for i in range(end, start, -1):
    print(i)


# The user types in two numbers.
# Print all numbers in the specified range in descending order.
 
start = int(input("start :"))
end = int(input("end :"))
 
for i in range(end, start -1, -3):
    print(i)
 
for i in range(start, end, 1):
    print(i)


# The user types in two numbers. 
# Print all odd numbers in the specified range. 
# If the end and start points of the range are incorrect, normalize them. 
# Let's say the user typed in 33 and 13, normalization will assign 13 to the start and 33 to the end of the range.

start = int(input("start :"))
end = int(input("end :"))
 
data = range(start, end)

for i in range(start, end +1):
    if i % 2 != 0 and start > end:
        print(i)


#v2


# The user types in two numbers.
#  Print all odd numbers in the specified range.
# If the end and start points of the range are incorrect, normalize them.
# Let's say the user typed in 33 and 13,
# normalization will assign 13 to the start and 33 to the end of the range.
 
start = int(input("start :"))
end = int(input("end :"))
 
if start > end :
    start, end = end , start
    data = range(start,  end+1)
else:
    data = range(start, end +1)
 
for i in data:
    if i % 2 != 0:
        print(i)
    

# szybkie rozwiązanie:
[print(i) for i in range(2, 20) if i % 2==0]
