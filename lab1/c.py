#Ex python list from w3schools
#1-chapter

#mylist = ['apple', 'banana', 'cherry']
#print(mylist[1])

#mylist = ['apple', 'banana', 'banana', 'cherry']
#print(mylist[2])

#EQ: List items cannot be removed after the list has been created.
#Ans: False

#thislist = ['apple', 'banana', 'cherry']
#print(len(thislist))


#2-chapter

#mylist = ['apple', 'banana', 'cherry']
#print(mylist[-1])

#fruits = ["apple", "banana", "cherry"]
#print(fruits[1])

#mylist = ['apple', 'banana', 'cherry', 'orange', 'kiwi']
#print(mylist[1:4])

#fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#print(fruits[2:5])


#3-chapter

#mylist = ['apple', 'banana', 'cherry']
#mylist[0] = 'kiwi'
#print(mylist[1])

#fruits = ["apple", "banana", "cherry"]
#fruits[0] = 'kiwi'
#print(fruits)

#mylist = ['apple', 'banana', 'cherry']
#mylist[1:2] = ['kiwi', 'mango']
#print(mylist[2])


#4-chapter

#mylist = ['apple', 'banana', 'cherry']
#mylist.insert(0, 'orange')
#print(mylist[1])

#fruits = ["apple", "banana", "cherry"]
#fruits.append("orange")
#print(fruits)

#fruits = ["apple", "banana", "cherry"]
#fruits.insert(1, "lemon")
#print(fruits)

#fruits = ['apple', 'banana', 'cherry']
#tropical = ['mango', 'pineapple', 'papaya']
#fruits.extend(tropical)
#print(fruits)


#5-chapter

#Q: What is a List method for removing list items?
#Ans: pop

#fruits = ["apple", "banana", "cherry"]
#fruits.remove('banana')
#print(fruits)

#mylist = ['apple', 'banana', 'cherry']
#mylist.pop(1)
#print(mylist)

#fruits = ['apple', 'banana', 'cherry']
#fruits.clear()
#print(fruits)


#6-chapter

#Q: What is a correct syntax for looping through the items of a list?
#for x in ['apple', 'banana', 'cherry']:
#  print(x)

#mylist = ['apple', 'banana', 'cherry']
#i = 0
#while i < len(mylist):
#  print(mylist[i])
#  i = i + 1

#Q: What is a correct syntax for looping through the items of a list?
#Ans: [print(x) for x in ['apple', 'banana', 'cherry']]


#7-chapter

#fruits = ['apple', 'banana', 'cherry']
#newlist = [x for x in fruits if x == 'banana']
#print(newlist)

#fruits = ["apple", "banana", "cherry"]
#newlist = [x for x in fruits]
#print(newlist)

#fruits = ['apple', 'banana', 'cherry']
#newlist = ['apple' for x in fruits]
#print(newlist)


#8-chapter

#Q: What is a correct syntax for sorting a list?
#Ans: mylist.sort()

#Q: What is a correct syntax for reversing the current order of a list?
#Ans: mylist.reverse()

#Q: What is a correct syntax for sorting a list descending?
#Ans: mylist.sort(reverse = True)


#9-chapter

#Q: What is a correct syntax for making a copy of a list?
#Ans: list2 = list1.copy()

#Q: What is a correct syntax for making a copy of a list?
#Ans: list2 = list(list1)

#Q: What is a correct syntax for making a copy of a list?
#Ans: list2 = list1[:]


#10-chapter

#Q: What is a correct syntax for joining list1 and list2 into list3?
#Ans: list3 = list1 + list2

#Q: What is a correct syntax for adding elements from list2 into list1?
#Ans: list1.extend(list2)

#list1 = ['a', 'b' , 'c']
#list2 = [1, 2, 3]
#for x in list2:
#  list1.append(x)
#  print(list1)

