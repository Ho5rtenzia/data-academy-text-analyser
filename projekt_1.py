"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Eva Vallušová
email: eva.vallusova@gmail.com
discord: energetic_avocado_65638
"""

import sys 
import task_template

section_splitter = "-" * 40

# Registration of users
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Texts for analysis
analysed_list = [None] + task_template.TEXTS
available_texts = len(analysed_list) - 1

# Name and password verification
your_username = input("username: ")
your_password = input("password: ")

if your_username.lower() in users and users[your_username.lower()] == your_password:
    print(section_splitter)
    print(f"Welcome to the app, {your_username}")
    print(f"We have {available_texts} texts to be analyzed.")
    print(section_splitter)
else:
    print("Unregistered user, terminating the program..")
    sys.exit()

#Selecting a text
try:
    number_of_text = int(input(f"Enter a number btw. 1 and {available_texts} to select: ")) 
    print(section_splitter)
    if number_of_text not in range(1, len(analysed_list)):
        print(f"Invalid number, please enter a number between 1 and {available_texts}")
        sys.exit()

    words_split = analysed_list[number_of_text].split()

    words_count = len(words_split)
    words_titlecase = 0
    words_uppercase = 0
    words_lowercase = 0
    words_number = 0
    sum_number = 0

    #for bar chart
    numbers_of_length = []
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
        words_length = len(word)
        occur.append(words_length)
        if words_length  not in numbers_of_length:
            numbers_of_length.append(words_length)

    sorted_length = sorted(numbers_of_length)

    # Results       
    print(f"There are {words_count} words in the selected text.")
    print(f"There are {words_titlecase} titlecase words.")
    print(f"There are {words_uppercase} uppercase words.")
    print(f"There are {words_lowercase} lowercase words.")
    print(f"There are {words_number} numeric values.")
    print(f"The sum of all numbers {sum_number}.")

    # Bar chart 
    print(section_splitter)

    max_stars_len = max(occur.count(lenght) for lenght in sorted_length)

    print(f"{'LEN':>3} | {'OCCURENCES':{max_stars_len + 2}} | NR.")
    print(section_splitter)
    
    for one_lenght in sorted_length:
        count_occurences = occur.count(one_lenght)
        stars = "*" * count_occurences 
        print(f"{one_lenght:>3} | {stars:{max_stars_len + 2}} | {count_occurences}")

except ValueError:
    print("Invalid input, please enter a number 1,2 or 3.")