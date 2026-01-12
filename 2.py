# strings
first_name = "Rishabh"
Last_name  = 'baruah'

long_string = """ this is a long string
that spans multiple lines """

age = 22

is_student = True
height = 5.9
print(first_name, Last_name, age, is_student, height)
print(long_string)
fullname = first_name + " " + Last_name
print("Full name is:", fullname)



# calculations
total = 10 - 8
power = 10 ** 2
print("Total:", total)
print("Power:", power)
long_dash = "-" * 10 
print(long_dash)

# built in functions
len(first_name)  # length of the string




# booleans
age = 16
can_vote = age>= 18 and is_student == False
print("Can vote:", can_vote)

# conditions
temperature = 25
if temperature > 30:
    print("It's a hot day")
elif temperature > 20:
    print("It's a nice day")
else:
    print("It's not a hot day")


# loops
for i in range(5):
    print("Iteration:", i)

#lists
fruits = ["apple",25 , "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)
fruits.append("orange")
print("Fruits list:", fruits)
fruits.remove(25)
name = fruits[1]

print("Name:", name)

# Dictionaries
person = {
    "name" : "Rishabh", 
    "age" : 22,
    "is_student" : True
}

person["age"] = 23


#Tuples :- they cannot be changed once created
coordinates = (10.0, 20.0)
print("Coordinates:", coordinates[0], coordinates[1])

# Sets :- they store unique values only
unique_numbers = {1, 2, 2, 3, 4, 4, 5}
print("Unique numbers:", unique_numbers)


# functions

def greet(name):
    print("hello " + name)

greet("Rishabh")
greet("Alice")


def checkweather(temp):
    if temp > 30:
        return "hot"
    elif temp > 20:
        return "nice"
    else:
        return "cold"
    
weather = checkweather(25)
print("The weather is:", weather)

# return 
def add(a, b):
    return a + b
result = add(5, 10)
print("Addition result:", result)


def double(number):
    return number * 2

sumof_double = double(5) + double(10)
print("Sum of doubles:", sumof_double)  