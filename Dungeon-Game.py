'''
This program is free software. It comes without any warranty, to
    * the extent permitted by applicable law. You can redistribute it
    * and/or modify it under the terms of the Do What The Fuck You Want
    * To Public License, Version 2, as published by Sam Hocevar. See
    * http://www.wtfpl.net/ for more details.
'''

#Because I need RNG
import random

#Cancer
pcharge = 0
echarge = 0

#White space
def spc():
    print(" ")

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

#Function for generating names.
def GenName():
    vowel = ["a", "e", "i", "o", "u"]
    const = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]

    def Set(x, y):
        x = RCG(x)
        y = RCG(y)
        z = x + y
        return z
    
    def Multiple():
        final = ""
        x = RNG(1, 3)
        final += Set(const, vowel)

        for i in range(x):
            #Visual studio was having a massive fit over i not being used.
            i = i
            y = RNG(1,4)

            if y == 1:
                final += Set(vowel, const)

            elif y == 2:
                final += Set(const, vowel)

            elif y == 3:
                final += random.choice(vowel)

            elif y == 4:
                final += random.choice(const)

        return final
    
    #Yay string slicing, definitely easy to understand and implent.
    x = Multiple()
    y = x[:1:]
    z = x[1::]
    y = y.upper()
    x = y + z

    return x

#I made the player name thing a function just for fun.
def GenPlayer():
    spc()
    name = str(input("What is your name?: "))
    if name == "" or name == " ":
        name = GenName()
    spc()

    #Player information
    player = {
        "Name" : name,
        "HP" : 100,
        "DF" : 50,
        "STR" : 25 }

    return player

#Checks if entity is 'dead' or not.
def IsDead(entity):
    HP = entity["HP"]

    if HP <= 0:
        return True

    else:
        return False

#Make enemy stats.
def GenEnemy():
    #I intend to make enemies scale with player and I intend to make bosses and elite/champion type enemies.
    enemy = {
        "Name" : GenName(),
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

#Make the enemy do stuff.
def EnemyMove(enemy, player):
    global echarge

    x = RNG(1, 10)

    if x == 1:
        DoDamage(enemy, player, RNG(20, 40))

    elif x == 2:
        z = RNG(1, 20)

        if z == 20:
            DoCrit(enemy, player, RNG(20, 40))

        elif z in range(1, 6):
            print(enemy["Name"] + " did some extra damage!")
            spc()
            DoDamage(enemy, player, RNG(25, 45))

    elif x == 3:
        print(enemy["Name"] + "'s head is in the clouds!")
        spc()

    elif x == 4 or x == 5:
        if echarge >= 2:
            print(enemy["Name"] + " wildy charges you!")
            spc()
            DoDamage(enemy, player, RNG(30, 55))
            echarge = 0

            return echarge

        else:
            print(enemy["Name"] + " is preparing something!")
            spc()
            echarge += 1

            return echarge
    
    elif x == 6:
        print(enemy["Name"] + " sneezes")
        spc()

def Help():
    Ask = str(input("Type a command for help: A, B, C, H, I, P: "))
    Ask = Ask.lower()
    spc()

    if Ask == "a":
        print("Deal damage to enemy.")
        spc()
        PlayerMove(player, enemy)

    elif Ask == "b":
        print("Increases stats exponentially (by a small margin), but you lose two turns each time you use it.")
        spc()

    elif Ask == "c":
        print("Build up a charged attack, once used three times, it activates.")
        spc()

    elif Ask == "h":
        print("Brings up the help prompt.")
        spc()
        PlayerMove(player, enemy)

    elif Ask == "i":
        print("Displays information on you and the enemy.")
        print("Player gets -1% to DF and enemy gets +1% to STR.")
        spc()

    elif Ask == "p":
        print("If the enemies next turn is an attack, you reflect all damage.")
        print("However, if it's not, all your stats are reduced.")
        spc()
        PlayerMove(player, enemy)

    else:
        print("You didn't input a valid command!")
        spc()
        PlayerMove(player, enemy)

#Player input logic stuff.
def PlayerMove(player, enemy):
    global pcharge
    global echarge

    ask = str(input("What do you do? Type H for help: "))
    spc()

    ask = ask.lower() 

    #Attack.
    if ask == "a":
        #Player has 1 in 20 chance to do crit and has 1 in 4 chance to do extra damage.
        x = RNG(1, 20)

        if x == 20:
            DoCrit(player, enemy, RNG(20, 40))

        elif x in range(1, 6):
            #Raise min so more damage is guranteed.
            print(player["Name"] + " did some extra damage!")
            spc()
            DoDamage(player, enemy, RNG(25, 45))

        else:
            DoDamage(player, enemy, RNG(20, 40))

    #Block.
    elif ask == "b":
        #Grab stats and do some pre-math.
        HP = player["HP"] / 100
        DF = player["DF"] / 100
        STR = player["STR"] / 100

        #Balance scale so it isn't op but still useful.
        scaleCalc = HP * STR * DF
        scaleCalc /= 8
        scaleCalc += 1

        #Multiply all the stats.
        HP *= scaleCalc
        DF *= scaleCalc
        STR *= scaleCalc

        #Round values.
        HP = RND(HP, 2)
        DF = RND(DF, 2)
        STR = RND(STR, 2)

        #And set the stats back to normal.
        HP *= 100
        DF *= 100
        STR *= 100
        
        #Round them again
        HP = RND(HP, 2)
        DF = RND(DF, 2)
        STR = RND(STR, 2)

        result = {"HP" : HP, "DF" : DF, "STR" : STR}

        player.update(result)

        EnemyMove(enemy, player)
        EnemyMove(enemy, player)

    #Charge.
    elif ask == "c":
        if pcharge >= 2:
            print(player["Name"] + " wildy charges " + enemy["Name"] + "!")
            spc()
            DoDamage(player, enemy, RNG(40, 60))
            pcharge = 0

            return pcharge

        else:
            print(player["Name"] + " is preparing something!")
            spc()
            pcharge += 1

            return pcharge

    #Help.
    elif ask == "h":
        Help()
        
    #Info.
    elif ask == "i":
        #Nerf info gathering a bit.
        DF = player["DF"]
        STR = enemy["STR"]
        DF /= 1.01
        STR *= 1.01
        DF = RND(DF, 2)
        STR = RND(STR, 2)
        p = {"DF" : DF}
        e = {"STR" : STR}
        player.update(p)
        enemy.update(e)

        print("You feel like you are slighty weaker now...")
        spc()

        print(player)
        spc()
        print(enemy)   
        spc()
        PlayerMove(player, enemy) 

    else:
        print("You didn't input a valid command!")
        spc()
        PlayerMove(player, enemy)

#Make the game work.
def Main():
    turn = 2

    player = GenPlayer()
    enemy = GenEnemy()

    while turn != 0:
        if IsDead(player) == True:
            print("You died!")
            spc()
            turn -= 1
            turn /= 2
            turn = RND(turn, 0)

            if turn <= 1:
                print("You lasted one turn! That or some error has occured!")

            else:
                print("You lasted " + str(turn) + " turns!")

            spc()
            turn = 0

        elif IsDead(enemy) == True:
            print(enemy["Name"] + " died!")
            spc()
            enemy = GenEnemy()
            print("Your new enemy is: " + enemy["Name"])
            spc()

        else:
            if turn % 2 == 0:
                PlayerMove(player, enemy)
                turn += 1

            else:
                EnemyMove(enemy, player)
                turn += 1

Main()