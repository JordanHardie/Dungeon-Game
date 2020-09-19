#Because I need RNG
import random

#Enter name
name = str(input("What is your name?: "))
spc()

#White space
def spc():
    print(" ")

#Player information
player = {
    "Name" : name,
    "HP" : 100,
    "DF" : 50,
    "STR" : 25
}
