# print:
print('I love you, michael.')

# variable:
age = 20
# print(age)
age = 30
# print(age)
my_first_name = 'Michael'
is_online = False
# print('Is ' + my_first_name + ' online ' + is_online.__str__())

# We check in a patient name Joshua
# He is 22 years old.
# He is a new patient.
# patient_name = input('What\'s your name? ')
patient_age = 22
new_patient = False

# print('How are you feeling today ' + patient_name)


# Type Conversion:
# age = input('How old are you?: ')
# birth_year = 2023 - int(age)
# print(birth_year)

# Simple Calculator:
# first_number = float(input('First: '))
# second_number = float(input('Second: '))
# sum = first_number + second_number
# print('Sum: ' + str(sum))


# Strings:
# laptop = 'Dell Latitude E3340'
# print(laptop.upper())
# print(laptop.find(' '))
# print(laptop.find('l'))
# print(laptop.replace('33', '2'))
# print(laptop.replace('z', 'me'))
# print(laptop.find('love'))
# print(laptop)


# Arithmetic Operators:
# print(10 ** 5)
x = 10
x += 3  # Augmented Assignment Operator

# Operator Precedence:
x = 10 + 3 * 2
# print(x)


# Comparison Operators:
x = 3 != 2
# print(x)

# Logical Operators:
price = 23
# print(not (price > 10 or price > 50))


# If Statements:
room_temperature = 40
# if room_temperature > 60:
#     print("It's a hot day")
#     print("Bath with cold water, not hot or warm water.")
# elif room_temperature > 20:
#     print("It's a nice day.")
# else: print("I hate hot weather.")

# weight = float(input("Weight: "))
# unit = input("(K)g or (L)bs: ").lower()
# if unit == "k":
#     kg = weight / 0.45
#     print("Weight in Kg: " + str(kg))
# elif unit == "l":
#     l = weight * 0.45
#     print("Weight in Lbs: " + str(l))
# else:
#     print("Invalid input")


# While Loops:
# i = 1
# while i <= 10:
#     print(i * "*")
#     i += 1

# List:
# Types of data: Numbers(Integers or Float), Boolean, String
# names = ["Michael", "Money", "Love", "Babe"]
# names[-1] = "Work Harder"
# new_year = names[2:4]
# print(new_year)


# List Methods:
numbers = [1, 2, 3, 2, 4, 5]
numbers.append(6)
numbers.insert(0, -1)
numbers.remove(4)
numbers.remove(2)
numbers.clear()
# print(len(numbers))


# For Loops:
# print("Printing a list with 'for loop'")
whole_numbers = [1, 2, 3, 4, 5]
for item in whole_numbers:
      item

# print("Printing a list with 'while loop'")
n = len(whole_numbers)
c = 0
while c < n:
    # print(whole_numbers[c])
    c += 1


# The range() Functions:
# range_numbers = range(5, 20, 3)
# print(range_numbers)
#
# for i in range_numbers:
#     print(i)
#
# print(len(range_numbers))


# Tuples
tuple_numbers = (1, 2, 3, 4, 5, 4, 4)
print(tuple_numbers.count(4))