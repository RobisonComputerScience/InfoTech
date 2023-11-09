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

#function will call the gasLevelGauge to determine gas level  and then find a close gas station if low
def gasLevelAlert():
   milesToGasStationsLow = random.uniform(a:1, b:25)

def gasLevelAlert():
    milesToGasStationsLow = round(random.uniform(1, 25), 1)
    milesToGasStationsQuarter = round(random.uniform(25.1, 50), 1)
    return gasLevelGauge
    if gasLevelGauge == "Empty Tank":
        print("***WARNING - YOU ARE ON EMPTY***")
        sleep(1.5)
        print("Calling Triple AAA")
    elif gasLevelGauge == "Low Tank":
        print("your gas tank is extremely low checking google maps for the closest gas station")