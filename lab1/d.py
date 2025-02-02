#Ex python tuple from w3schools
#1-chapter

#Q: Which one of these is a tuple?
#Ans: thistuple = ('apple', 'banana', 'cherry')

#fruits = ("apple", "banana", "cherry")
#fruits = ("apple", "banana", "cherry")
#print(len(fruits))

#Q: Tuple items cannot be removed after the tuple has been created.
#Ans: True


#2-chapter

#Q: You can access tuple items by referring to the index number, but what is the index number of the first item?
#Ans: 0

#fruits = ("apple", "banana", "cherry")
#print(fruits[0])

#fruits = ("apple", "banana", "cherry")
#print(fruits[-1])

#fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
#print(fruits[2:5])


#3-chapter 

#Q: You cannot change the items of a tuple, but there are workarounds. Which of the following suggestion will work?
#Ans: Convert tuple into a list, change item, convert back into a tuple.

#Q: Which is a correct syntax to delete a tuple?
#Ans: del mytuple

#Q: True or False. You are allowed to add a tuple to an existing tuple.
#Ans: True


#4-chapter

#fruits = ('apple', 'banana', 'cherry')
#(x, y, z) = fruits
#print(y)

#fruits = ('apple', 'banana', 'cherry')
#(x, *y) = fruits
#print(y)

#fruits = ('apple', 'banana', 'cherry', 'mango')
#(x, *y, z) = fruits
#print(y)


#5-chapter

#Q: What is a correct syntax for looping through the items of a tuple?
#Ans: for x in ('apple', 'banana', 'cherry'):
#   print(x)

#mytuple = ('apple', 'banana', 'cherry')
#i = 0
#while i < len(mytuple):
#  print(mytuple[i])
#  i = i + 1

#thistuple = ("apple", "banana", "cherry")
#for i in range(len(thistuple)):
#  print(thistuple[i])

#6-chapter

#Q: What is a correct syntax for joining tuple1 and tuple2 into tuple3?
#Ans: tuple3 = tuple1 + tuple2

#Q: What is a legal way to turn this tuple: (1,2,3) into this tuple:(1,2,3,1,2,3)?
#Ans: tuple1 = (1,2,3)
# tuple1 = tuple1 * 2

#tuple1 = ('a', 'b' , 'c')
#tuple2 = (1, 2, 3)
#tuple3 = tuple2 + tuple1
#print(tuple3)