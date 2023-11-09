"""
Our Welcome Screen will start our program letting
drivers know that the Infotech Center 2023 is loading
"""
#Libraries Here
import time
import sys
import random
from time import sleep


timeToSleep = 2

print("\nWelcome - InfoTech Center 2023")
time.sleep(timeToSleep)

#add code to have the ellipsis add a dot every .5 seconds
x = 0
ellipsis = 0

while x != 20:
    x += 1
    message = ("InfoTech Center 2023 is loading" + "." * ellipsis)
    ellipsis = ellipsis + 1
    sys.stdout.write("\r" + message) # \r prints a carriage return first so message stays on same line
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis = 0
    if x ==20:
        print("\n\n Operating system loaded\n")

print("**************************************************************\n")
print("Checking current gasoline levels.\n")

sleep(1)

# function that list gas stations and randomly chooses one, and then returns its value
def gasLevelGauge():
    gasLevelList = ["Empty Tank","Low Tank","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

# Function with a list of GasStations
def listOfGasStations():
    gasStations = ["Shells","Speedway", "Exxon", "Seven Eleven", "Meijer", "Costco" ,"Marathon", "BP", "cirlce K", "Wesco"]
    gasStationsNearby = random.choice(gasStations)
    return gasStationsNearby

#function will call the gasLevelGauge to determine gas level  and then find a close gas station if low
def gasLevelAlert():
    milesToGasStationsLow = round(random.uniform(1, 25), 1)
    milesToGasStationsQuarter = round(random.uniform(25.1, 50), 1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty Tank":
        print("You're on empty Womp Womp shoulda gotten gas")
        sleep(.5)
        print("Calling Triple AAA")
    elif gasLevelIndicator == "Low Tank":
        print("Your gas tank is extremely low, checking google maps for the closest gas station")
        sleep(.5)
        print("The closest gas station is", listOfGasStations(), "Which is",milesToGasStationsLow, "miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is about a quarter of a tank, checking google maps for the closest gas station")
        sleep(.5)
        print("The closest gas station is", listOfGasStations(), "Which is", milesToGasStationsQuarter, "miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("your gas tank is about half of a tank.")
        sleep(.5)
        print("The closest gas station is", listOfGasStations(), "Which is", milesToGasStationsLow, "miles away.")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("You're on a three quarters of a tank You'll make it")
    else:
        print("WOOO you're on a full tank")



gasLevelAlert()


