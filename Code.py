# name = str(input("Whos birhday?" ))
# age = int(input("How old are they getting?" ))

# def happy_birthday(name, age):
#     print(f"Happy Birtday To {name}!")
#     print(f"You are getting {age} years old!")

# happy_birthday(name, age)
#-------------------------------------- 

# def display_invoice(username, amount, due_date):
#     print(f"Hello{username}")
#     print(f"Your bill of ${amount} is due: {due_date}")

# display_invoice("Jack",69.42, "01/02")
#----------------------------------------

# def create_name(first, last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first + " " + last

# first = input(str("First Name?"))
# last = input(str("Last Name?"))


# full_name = create_name(first, last)
# print(full_name)
#-------------------------------- 

# lenght = float(input("Enter lenght of rectangle(m); "))
# width = float(input("Enter width of rectangle(m); "))
# height = float(input("Enter the height of rectangle(m); "))

# volume = lenght * width * height

# print(f"The Area is {volume}m^3")
#-------------------------------- 

# start = int(input("Enter a number(>1); "))
# slut = int(input("Enter a number greater then the first; "))

# def numbers_between(start, slut):
#     for num in range(start +1.0, slut):
#         print(num, end=" ")
#     if start == 0 or slut == 0:
#         print("Error")
#         start_1 = int(input("Enter a diffrent number; "))
#         slut_1 = int(input("Enter a  number; "))
#         for num_1 in range(start_1 +1, slut_1):
#             print(num_1)
#     else:
#         print("ReRun program")

# numbers_between(start, slut)
#-------------------------------------------------------- 

# health = float(input("How much health do you have? "))
# def is_alive(health):
#     if health > 0:
#         print("You are alive(True)")
#     elif health < 0:
#         print("You are dead(False)")
#     elif health == 0:
#         print("You are dead(False)")

# is_alive(health)
#--------------------------------------------------

# lista = list(range(1,101))
# for i in lista:
#     if i % 3 == 0 and i % 5 == 0:
#         print("Fizz Buzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print (i)

#------------------------------------------ 
# str = "He was going to live forever, or die in the attempt"

# print (str.count("e"))
#------------------------------------------
# namn = str(input("name? "))

# print(namn[::-1])
#----------------------------------------- 

# text = str(input("ord?: "))

# def rovar_sprak(text):
#     vowels = "aeiouyåäöAEIOUYÅÄÖ"
#     result = ""

#     for char in text:
#         if char.isalpha() and char not in vowels:
#             result += char + "o" + char.lower()
#         else:
#             result += char

#     return result

# print(rovar_sprak(text))
#------------------------------------------- 
# min_lista = [17, 8, 25, 10, 1, 3]

# print(min_lista[2])
# min_lista.append(3)

# min_lista.sort()
# print (min_lista)
#-------------------------------------------
