import string
import json

# Define character set
char = string.ascii_letters + string.digits + string.punctuation

# Read the key from key.txt
with open("key.txt", "r") as file:
    key = file.read()

with open("passwords.json", "r") as f:
    passes = json.load(f)



def adder():
    print("Add a new password: ")
    #Asks user for the site / password
    site = input("For what Website: ")
    ine = input("Whats the password: ")
    text = ""
    for letter in ine:
        if letter in char:
            index = char.index(letter)
            text += key[index]
        else:
            text += letter
    passes[site] = text
    with open("passwords.json", "w") as f:
        json.dump(passes, f, indent=2)
    print("done")



def finder():
    site = input("What site: ")
    if site in passes:
        get = passes[site]
        text = ""
        for letter in get:
            if letter in key:
                index = key.index(letter)
                text += char[index]
            else:
                text += letter
        print(text)
    else:
        print("No password found for " + site)


print("Do you want to add or find a password(s):")
ask = input("1) Add     2) Find: ")


if ask == "1":
    adder()

elif ask == "2":
    finder()

else:
    print("Sorry wrong input please try agin.")