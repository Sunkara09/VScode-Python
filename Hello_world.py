# What is the value of x + y?
x = 10
y = 5
print(x + y)

# Create a variable full_name that combines first_name and last_name with a space in between.
first_name = "John "
last_name = "Doe"
print(first_name + last_name)

# Convert variable a to an integer and store it in a new variable.
a = "123"
A = int(a)
print(A)
print(type(A))

# Swap the values of x and y without using a third variable.
x = 3
y = 7
x, y = y, x
print(x)
print(y)

# Increase counter by 1 five times using +=
counter = 0
counter += 1
counter += 1
counter += 1
counter += 1
counter += 1
print(counter)

# Assign the values 1, 2, 3 to variables a, b, c in one line.
a, b, c = 1, 2, 3
print( a, b, c)
print(a)
print(b)
print(c)

x = 100
def test():
    y = 200
    print(globals()['x'])  # What is printed?
    print(locals()['y'])   # What is printed?
test()

# Print "Alice is 25 years old" using the variables.
name = "Alice"
age = 25
print(f"{name} is {age} years old.")


# Ask the user to enter their age and store it in a variable called user_age.
user_age = int(input("Enter your age:"))
print(user_age)

# Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
spam = 10
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')
