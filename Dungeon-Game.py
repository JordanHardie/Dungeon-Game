#Because I need RNG
import random

turn = 2

#White space
def spc():
    print(" ")

#Enter name
spc()
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

#More shorthand.
def RND(x, y):
    result = round(x, y)
    return result

#Make enemy stats.
def GenEnemy():
    enemy = {
        "Name" : nameGen(),
        "HP" : RNG(75, 150),
        "DF" : RNG(30, 70),
        "STR" : RNG(20, 30)
    }

    return enemy

#Does math for stat stuff
def statCalc(From, To):
    STR = From["STR"]
    DF = To["DF"]

    DF = float (DF / 100)
    STR += 100
    STR = float(STR / 100)

    result = {"DF" : DF, "STR" : STR}

    return result

#Do damage from entity to entity.
def DoDamage(From, To, dmg):
    get = statCalc(From, To)
    HP = To["HP"]
    STR = get["STR"]
    DF = get["DF"]

    atkcalc = dmg * STR
    adj = atkcalc * DF

    X = RND(adj, 0)
    HP -= X
    HP = RND(HP, 0)

    X = str(X)

    print(From["Name"] + " did " + X + " dmg to " + To["Name"] + ".")
    spc()
    result = {"HP" : HP}
    To.update(result)

#Increase damage done from entity to entity.
def DoCrit(From, To, dmg):
    get = statCalc(From, To)
    HP = To["HP"]
    STR = get["STR"]
    DF = get["DF"]
 
    #Generate critical damage multiplier 
    crit = RNG(125, 200)
    crit = float(crit / 100)

    dmg = dmg * STR
    atkcalc = dmg * crit
    #Pfft, I didn't increase DF to balance the OP'ness of the crit
    adj = atkcalc * (DF + 0.1)

    X = RND(adj, 0)
    HP -= X
    HP = RND(HP, 0)
    
    X = str(crit)

    print(From["Name"] + " had their dmg multipied by " + X + "x.")
    spc()
    result = {"HP": HP}
    To.update(result)

#Function for generating enemy names.
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

def playerMove(player, enemy):
    ask = str(input("What do you do? Type H for help: "))
    spc()

    if ask.lower() == "h":
        Ask = str(input("Type a command for help: A, H. : "))

        if Ask.lower() == "a":
            print("Deal damage to enemy")
            spc()
            playerMove(player, enemy)

        elif Ask.lower() == "h":
            print("Get help menu command")
            spc()
            playerMove(player, enemy)

        else:
            print("You didn't input a valid command!")
            spc()
            playerMove(player, enemy)

    elif ask.lower() == "a":
        x = RNG(1, 20)

        if x == 20:
            DoCrit(player, enemy, RNG(20, 40))

        elif x == 10:
            DoDamage(player, enemy, RNG(25, 45))

        else:
            DoDamage(player, enemy, RNG(20, 40))

    elif ask.lower() == "b":
        print("Blocked!")
        spc()

    else:
        print("You didn't input a valid command!")
        spc()
        playerMove(player, enemy)


def enemyMove(enemy, player):
    x = RNG(1, 10)

    if x == 1:
        DoDamage(enemy, player, RNG(20, 40))

    elif x == 2:
        y = RNG(1, 20)
        if y == 20:
            DoCrit(enemy, player, RNG(20, 40))

        else:
            DoDamage(enemy, player, RNG(25, 45))

    elif x == 3:
        print(enemy["Name"] + "'s head is in the clouds!")
        spc()

    elif x == 4:
        print(enemy["Name"] + " is preparing something!")
        spc()

def Main(turn):
    enemy = GenEnemy()

    while turn != 0:
        if turn % 2 == 0:
            playerMove(player, enemy)
            turn += 1

        elif turn % 2 == 1:
            turn += 1

Main(turn)