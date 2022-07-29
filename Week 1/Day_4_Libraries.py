#V1
import random as rand
from math import sqrt, pow

r1=pow(15,2)
print(r1)

r2=sqrt(123)
print(r2)

r3=rand.randint(0,10000)
print(r3)

numbers=[1,2,3,4,5,6,7,8,9,0]
print(numbers)
rand.shuffle(numbers)
print(numbers)

r4=rand.choice(numbers)
print(r4)


#V2
import random
import math

r1=math.pow(15,2)
print(r1)

r2=math.sqrt(123)
print(r2)

r3=random.randint(0,10000)
print(r3)

numbers=[1,2,3,4,5,6,7,8,9,0]
print(numbers)
random.shuffle(numbers)
print(numbers)

r4=random.choice(numbers)
print(r4)

#V2
from random import choice, shuffle, randint as choice, shuffle, randint
import math as math

r1=pow(15,2)
print(r1)

r2=sqrt(123)
print(r2)

r3=rand.randint(0,10000)
print(r3)

numbers=[1,2,3,4,5,6,7,8,9,0]
print(numbers)
rand.shuffle(numbers)
print(numbers)

r4=rand.choice(numbers)
print(r4)