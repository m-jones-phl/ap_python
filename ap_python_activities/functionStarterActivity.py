# 1. In your own words, describe what a function is
<<<<<<< HEAD
peices of code you can reuse /  reuse instructions 
# 2. What is are function parameters and arguments and describe
# the difference between the 2.
A parameter is a variable in a function. It is a placeholder. 
An argument is a value passed during function invocation. 
# 3. write a function that will print out a welcome message
# that includes a users name. You will need to use parameters and arguments
user_name = input("Enter your name:-")
print("Welcome to school,",jeff,"\b!")
=======
# a way to store a peice of code  that does  a task
# 2. What is are function parameters and arguments and describe
# the difference between the 2 is that a variable is a function

# 3. write a function that will print out a welcome message
# that includes a users name. You will need to use parameters and arguments

def isClassOver(timeParameter):
    if timeParameter>11.30:
        print('class is over. Time to go.')
    else:
        print('no, lets keep going')

isClassOver(11.31)
>>>>>>> a486cd4 (my work , the changwe was my name)
# 4. Write a function that will do a calculation that takes 3 parameters.
# Your function can do any of the arithmatic operators (add, subtract, multiply, divide)
def addition():
if string == "+":
    a = num10 + num20
    print("addition was performed on the two numbers ", num10, ' and ', num20)
    return a

def subtraction():
if string == "-":
    s = num1 - num2
    print("subtraction was performed on the two numbers ", num1, ' and ', num2)
    return s

def multiplication():
if string == "*":
    t = num20 * num50
    print("multiplication was performed on the two numbers ", num20, ' and ', num50)
    return t

def division():
if string == "/":
    d = num1 / num2
    print("division was performed on the two numbers ", num1, ' and ', num2)
    return d

def writeName(nameParameter):
    user_name= input('what is your name?')
    if not isinstance(nameParameter, (int, float)): 
        print('cannot be a number')
    else:
        print('hello ' + user_name)

#writeName('leek')

# 5. Write a function that will output a message to a user, telling them
# what class they have next after this one. this code should use a 
# variable to pass a value into the parameter of a function. The variable should
# be real, user data- not hard coded data.

<<<<<<< HEAD
def getClass():
   name = "biology"
   return name
=======
def petNoise(petParameter):
    if petParameter== 'dog':
        print('woof woof')
    elif petParameter =='cat':
        print('meow')

#petNoise('ruff')
>>>>>>> a486cd4 (my work , the changwe was my name)

