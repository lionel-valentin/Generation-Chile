mystring="This is a string"
print(mystring)
print(type(mystring))
print(mystring + " is of the date type " + str(type(mystring)))

firstString="water"
secondString="fall"
thridString=firstString + secondString
print(thridString)

name=input("What is your name?: ")
print(name)

color=input("What is your favorite color?: ")
animal=input("What is your favorite animal?: ")
print("{}, you like a {} {}!".format(name,color,animal))
print(f"{name}, you like a {color} {animal}!")