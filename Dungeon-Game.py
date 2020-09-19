#Because I need RNG
import random

#White space
def spc():
    print(" ")

#Enter name
name = str(input("What is your name?: "))
spc()

#Player information
player = {
    "Name" : name,
    "HP" : 100,
    "DF" : 50,
    "STR" : 25
}

#I want to include both end points just to make things easier and less confusing.
def RNG(x, y):
    result = random.randint(x, y)
    return result

#Shorthand to make things easier.
def RCG(x):
    result = random.choice(x)
    return result

def GenEnemy():
    enemy = {
        "Name" : nameGen(),
        "HP" : RNG(75, 150),
        "DF" : RNG(30, 70),
        "STR" : RNG(20, 30)
    }

    return enemy

#Function for generating enemy names
def nameGen():
    vowel = ["a", "e", "i", "o", "u"]
    const = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]

    def set(x, y):
        x = RCG(x)
        y = RCG(y)
        z = x + y
        return z
    
    def multiple():
        final = ""
        x = RNG(1, 3)
        final += set(const, vowel)

        for i in range(x):
            #Visual studio was having a massive fit over i not being used.
            i = i
            y = RNG(1,4)

            if y == 1:
                final += set(vowel, const)

            elif y == 2:
                final += set(const, vowel)

            elif y == 3:
                final += random.choice(vowel)

            elif y == 4:
                final += random.choice(const)

        return final
    
    #Yay string slicing, definitely easy to understand and implent.
    x = multiple()
    y = x[:1:]
    z = x[1::]
    y = y.upper()
    x = y + z

    return x
