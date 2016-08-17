import math
import random

x = input("The average IQ of a Trump Supporter: " )
#sure this input serves no purpose but does anyone really care?
y = 0
y = random.randint(1,100)


def medoutput(y):
    if  1 <= y <=10:
        print("my hemoglobin is the reddest")
    elif 11 <= y <=20:
        print("my prostate is yyyyuuuuggge")
    elif 21 <= y <=30: 
        print("my glucose is the best")
    elif 31 <= y <=40: 
        print("my white blood cells impress David Duke")
    elif 41 <= y <=50: 
        print("my white blood cells impress David Duke")
    elif 51 <= y <=60: 
        print("My hands are so big I can build the wall myself")
    else:
        print("the doctor says 1 finger isn't enough better make it the whole fist")

medoutput(y)
        
