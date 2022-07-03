# Notes from Corey Schafer's Python Course
# https://www.youtube.com/c/Coreyms

#Set string var
greeting = "Hello"
name = "Joe"

#Concatenate
message = greeting + " " + name + ". Welcome!"

#Format method
#message = "{}, {}. Welcome!".format(greeting, name)

#f strings (New to python)
#message = f'{greeting}, {name.upper()}. Welcome!'
#print(message)

#Print all methods and attribs that can run with the var.
#print(dir(name))

#help all string methods
#print(help(str))

#help string lower method
#print(help(str.lower))

num = 3
print (type(num))

num1 = 3.14
print (type(num1))

#Operators

# / division new in 3..adds dec
print (3 / 2)

# Floor // drop remain
print ( 3 //2 )

# Exponent **
print( 3 ** 2)
# 9

# Mod %
# by 2 if 0 even
# by 2 if 1 odd 
print ( 3 % 2)
# remain of 1

num = 1 
# same
num = num + 1
num += 1

num *= 10
#10

#ABS 
# absolute value..removes negative
print(abs(-3))

# Round
# Round nearest to int value
print(round(3.74))
# prints 4

# overloaded method, can add nearest dec
print(round(3.75, 1))
# 3.8

# Comparisons
# Equal: 3 ==  2
# Not Equal: 3 != 2
# Grater Than: 3 > 2
# Less Than: 3 < 2
# Greater Than or Equal to: 3 >= 2
# Less or Equal: 3 <= 2

num1 = 3
num2 = 2

print(num1 == num2)
#returns false

#Casting
num_1 = "100"
num_2 = "200"
print(num_1 + num_2)
#prints 100200. 
# Need to cast from string to int
num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2)
# Prints 300




