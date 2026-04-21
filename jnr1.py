data = {
    'first name': 'john',
    'last name' : 'Doe',
    'age':45,
    'friends':['maria', 'sofia', 'carol']
}
 
friend = data['friends']
for i in friend:
    print(i)
# print(friend)

# definition :- a collection of data with keys and value pairs

bookDict = {'author':'Eric Matthes',
            'title':'Python Crash Course',
            'price':14.43,
            'reading age':'12 years and up',
            'language':'English'
           }
 
# print(bookDict['author'])
 
for i in bookDict:
    # print(i)
    print(bookDict[i])


# The user types in a string.
# Rotate the strings and display the result.
 
# user_input = input("please provide an input:")
 
 
# start,: end,: step
# data = [1,2,3,4,5,56,13]
# data = "pushkar"
data= (1,2,3,4,5,6,7,8)
print(data[::-1])
 
# reversed = user_input[::-1]
# print(reversed)


user_input = input("please provide an input:")


user_input =input("please provide a input with numbers and digits")
 
alphabets = 0
nums = 0
 
for i in user_input:
        if i.isalpha():
            nums += 1
        elif i.isdigit():
            alphabets += 1
 
print(alphabets)
print(nums)


# The user types in a string and a symbol to be searched for.
# Count how many times this symbol appears in the string. Print the result.
 
user_input = input("string with symbol :")
symbol = input("symbol :")
 
count_symbol = 0
for i in user_input:
    if i == symbol:
        count_symbol += 1
       
print(f"{symbol} was found {count_symbol} times in a string")

# The user types in a string, a search word, and a replacement word. 
# Replace one word with another one in the string. Print the resulting string.


user_input = input("provide the sentence: ")
word_to_replace = input("word to replace: ")
replacement_word = input("replacement word: ")

output = string.replace(search_word, replacement_word)
print(string)
print(output)

# https://www.w3schools.com/python/ref_string_replace.asp
