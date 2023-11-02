print("**************************************************************")
print("Gasoline Branch\n\n")

# Import Libraries here
import random
from time import sleep
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
        print("Womp Womp shoulda gotten gas")
        sleep(1.25)
        print("Calling Triple AAA")
    elif gasLevelIndicator == "Low Tank":
        print("your gas tank is extremely low, checking google maps for the closest gas station")
        sleep(1.5)
        print("The closest gas station is", listOfGasStations(), "Which is",milesToGasStationsLow, "miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("your gas tank is about a quarter of a tank, checking google maps for the closest gas station")
        sleep(1.5)
        print("The closest gas station is", listOfGasStations(), "Which is", milesToGasStationsQuarter, "miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("your gas tank is about half of a tank.")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("You'll make it")
    else:
        print("WOOO")



gasLevelAlert()

