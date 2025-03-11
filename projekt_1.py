"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Eva Vallušová
email: eva.vallusova@gmail.com
discord: energetic_avocado_65638
"""

# Registration of users
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Importing text for analysis
import task_template
analysed_list = [None] + task_template.TEXTS

# Name and password verification
your_username = input("username:")
your_password = input("password:")
split_ = "-" * 40

if your_username.lower() in users and users[your_username.lower()] == your_password:
    print(f"username: {your_username}")
    print(f"password: {your_password}")
    print(split_)
    print(f"Welcome to the app, {your_username}")
    print("We have 3 texts to be analyzed.")
    print(split_)
else:
    print(f"username: {your_username}")
    print(f"password: {your_password}")
    print("Unregistered user, terminating the program..")
    exit()

#Selecting a text
try:
    number_of_text = int(input("Enter a number btw. 1 and 3 to select:  ")) 
    print(split_)
    if number_of_text not in range(1, len(analysed_list)):
        print("Invalid number, please enter 1,2 or 3.")
        exit()

    words_split = analysed_list[number_of_text].split()

    words_count = len(words_split)
    words_titlecase = 0
    words_uppercase = 0
    words_lowercase = 0
    words_number = 0
    sum_number = 0

    #for bar chart
    numbers_of_lenght = []
    occur = []

    for word in words_split:
        word = word.strip(".,!?()[]{}:;\"')")
        if word.istitle():
            words_titlecase += 1
        elif word.isupper() and word.isalpha():
            words_uppercase += 1
        elif word.islower():
            words_lowercase += 1

        try:
            number = int(word)
            words_number += 1
            sum_number += number
        except ValueError:
            pass
        
        #Calculation of word length frequency
        words_lenght = len(word)
        occur.append(words_lenght)
        if words_lenght not in numbers_of_lenght:
            numbers_of_lenght.append(words_lenght)

    sorted_length = sorted(numbers_of_lenght)

    # Results       
    print(f"There are {words_count} words in the selected text.")
    print(f"There are {words_titlecase} titlecase words.")
    print(f"There are {words_uppercase} uppercase words.")
    print(f"There are {words_lowercase} lowercase words.")
    print(f"There are {words_number} numeric values.")
    print(f"The sum of all numbers in the text is {sum_number}.")

    # Bar chart 
    print("LEN|  OCCURENCES  |NR.")
    print(split_)
    for one_lenght in sorted_length:
        stars = "*" * occur.count(one_lenght)
        print(f"{one_lenght:>3} | {stars:<13} | {occur.count(one_lenght)}")
    print(split_)

except ValueError:
    print("Invalid input, please enter a number 1,2 or 3.")