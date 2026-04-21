# TASK 1:

X = int(input("Number 1:"))
Y = int(input("Number 2:"))

print(X ** Y)

# TASK 2:

count = 0

for number in range(100, 1000):

    cyfra1 = str(number)[0]
    cyfra2 = str(number)[1]
    cyfra3 = str(number)[2]

    if cyfra1 == cyfra2 and cyfra1 != cyfra3:
        count += 1
    elif cyfra1 == cyfra3 and cyfra1 != cyfra2:
        count += 1
    elif cyfra2 == cyfra3 and cyfra2 != cyfra1:
        count += 1

print("Numbers with two identical digits:", count)

# TASK 3:

count = 0

for number in range(100, 10000):

    number_str = str(number)

    if len(number_str) == len(set(number_str)):
        count += 1

print("Numbers with different digits:", count)

# TASK 4:

number = int(input("Provide the number: "))

number_str = str(number)

result = ""

for digit in number_str:

    if digit != '3' and digit != '6':
        result += digit
print("Result after removal 3 and 6:", result)
