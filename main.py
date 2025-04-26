import random

print('Hello World !!!')  # basics

def getMoodFoodOfTheDay():
    userValue = input("Enter what type of food to consume : F for Fancy mood , N for Normal mood : ")
    print(userValue)

    if(userValue=='N'):
        getNormalFood()
    elif (userValue =='F') :
        getFancyFood()

    getAsthetics()



def getAsthetics():
    print("Dryfuit of the day : " + getRandomDiet("DryFruit.txt"))
    print("Outfit of the day : " + getRandomDiet("TshirtToday.txt"))


def getRandomDiet(fileName):
    sabji = open(fileName).read().splitlines()
    return random.choice(sabji)

def getFancyFood():

    fVal = input("Kindly type 'A' for around the world and 'I' for Indian fancy dishes : ")
    if (fVal == 'A'):
        print("Fancy food of the day : " + getRandomDiet("AroundTheWorld.txt"))
    elif (fVal == 'I'):
        print("Fancy food of the day : " + getRandomDiet("IndianFancyFood.txt"))
        print("Side of the day : " + getRandomDiet("IndianSides.txt"))

def getNormalFood():
    print("Shak of the day : " + getRandomDiet("gujjuSabji.txt"))
    print("Bread of the day : " + getRandomDiet("IndianBread.txt"))


getMoodFoodOfTheDay()   

# Problem definition
# Read from .properties file if py supports that
# Week
# Dish
# Breads
# Bevrage


# kariye che
