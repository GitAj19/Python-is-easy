"""Python Homework #4 - Lists"""

import functions

myUniqueList = []
myLeftovers = []

functions.addToList(myUniqueList, myLeftovers, 45)
functions.addToList(myUniqueList, myLeftovers, 75)
functions.addToList(myUniqueList, myLeftovers, "Hello")
functions.addToList(myUniqueList, myLeftovers, 1.05)
functions.addToList(myUniqueList, myLeftovers, 45)
functions.addToList(myUniqueList, myLeftovers, "Pirple")
functions.addToList(myUniqueList, myLeftovers, "Python")
functions.addToList(myUniqueList, myLeftovers, 0.34)
functions.addToList(myUniqueList, myLeftovers, "Python")
functions.addToList(myUniqueList, myLeftovers, 45)

print("My unique list:", end=" ")
print(myUniqueList)
print("My leftovers:", end=" ")
print(myLeftovers)
