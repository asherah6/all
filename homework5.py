# Task 1
# Create an app that stores information about great basketball players. 
# Store the player's full name and height. 
# Provide the possibility to add, delete, search, and replace data. 
# Use a dictionary to store information.


players = {}  
  
while True:  
    action = input("\n(add, del, search, replace, exit): ").lower()  
  
    if action == "exit":  
        print("Good bye!")  
        break  
  
    name = input("Player name: ")  
  
    if action == "add" or action == "replace":  
        height = input("Height: ")  
        players[name] = height  
        print("Done!")  
  
    elif action == "del":  
        if name in players:  
            players.pop(name)  
            print("Deleted!")  
        else:  
            print("Not found!")  
  
    elif action == "search":  
        print(name, ":", players.get(name, "Not found!"))


# Task 2
# Create an app English-French Dictionary. Store a word in English and its French translation. 
# Provide the possibility to add, delete, search, and replace data. 
# Use a dictionary to store information.

dictionary = {}  
  
while True:  
    action = input("\n(add, del, search, replace, list, exit): ").lower()  
  
    if action == "exit":  
        print("Good bye!")  
        break  
  
    elif action == "list":  
        if len(dictionary) == 0:  
            print("Dictionary is empty!")  
        else:  
            for eng, fr in dictionary.items():  
                print(eng, "->", fr)  
  
    else:  
        english = input("English word: ")  
  
        if action == "add" or action == "replace":  
            french = input("French translation: ")  
            dictionary[english] = french  
            print("Done!")  
  
        elif action == "del":  
            if english in dictionary:  
                dictionary.pop(english)  
                print("Deleted!")  
            else:  
                print("Not found!")  
  
        elif action == "search":  
            print(english, "->", dictionary.get(english, "Not found!"))


# Task 3
# Create an app Company. 
# Store the following information about a person: 
# full name, phone number, corporate email, job title, room number, skype. 
# Provide the possibility to add, delete, search, and replace data. 
# Use a dictionary to store information.

company = {}  
  
while True:  
    action = input("\n(add, del, search, replace, exit): ").lower()  
  
    if action == "exit":  
        break  
  
    name = input("Full name: ")  
  
    if action == "add" or action == "replace":  
    
        company[name] = {  
            "phone": input("Phone: "),  
            "email": input("Email: "),  
            "job": input("Job: "),  
            "room": input("Room: "),  
            "skype": input("Skype: ")  
        }  
        print("Done!")  
  
    elif action == "del":  
        if name in company:  
            company.pop(name)  
            print("Deleted!")  
        else:  
            print("Not found!")  
  
    elif action == "search":  
        if name in company:  
            print(name, ":", company[name])  
        else:  
            print("Not found!")


# Task 4
# Create an app Book Collection. 
# Store the following information about books: 
# author, title, genre, year of release, publisher. 
# Provide the possibility to add, delete, search, and replace data. 
# Use a dictionary to store information.

books = {}  
  
while True:  
    action = input("\n(add, del, search, replace, exit): ").lower()  
  
    if action == "exit":  
        print("Good bye!")  
        break  
  
    title = input("Book title: ")  
  
    if action == "add" or action == "replace":  
        books[title] = {  
            "author": input("Author: "),  
            "genre": input("Genre: "),  
            "year": input("Year of release: "),  
            "publisher": input("Publisher: ")  
        }  
        print("Done!")  
  
    elif action == "del":  
        if title in books:  
            books.pop(title)  
            print("Deleted!")  
        else:  
            print("Not found!")  
  
    elif action == "search":  
        if title in books:  
            print(title, ":", books[title])  
        else:  
            print("Not found!")