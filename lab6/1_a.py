import cmath
import re
import random
#number_a=random.randint(0,100)
#number_b=random.randint(0,100)
#number_c=random.randint(0,100)
#print(number_a*number_b*number_c) 

#numbers = [random.randint(1, 10) for _ in range(3)]
#product = 1

#for num in numbers:
#    product *= num

#print(numbers)
#print(product)


#txt=open('lab6_a.txt')
#file = open('lab6_a.txt','r')
#file = open('second.txt','a')
 
#file.write("1\n")
 
#print(file.readline())
#print(file.readline())

with open("lab6_a.txt", "r") as f:
    score = f.read() 
    score_ints = [ int(x) for x in score.split() ] # Convert strings to ints I take from site
    print (sum(score_ints)) 


 