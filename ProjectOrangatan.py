print("\n******************************************")

print("Weather Brnach\n")

#import Libraries here
import random
from time import sleep
#create a function randomly choosing the weather from a list
def weather():
    weatherForecast = ["Snowing","Blizzard","Rain","Foggy","Windy","Icy","Sunny","Cloudy"]
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition

#variable to call weather() once in our Vehicle Response System - VRS
weatherAlert = weather()

#VRS() Function will allow my vehicle to respond based weather conditions
def vehicleResponseSystem():
    if weatherAlert =="Snowing":
        print("National weather service has updated your alarm by 30 minutes because of the forcast of",weatherAlert)
        print("Vehicle Response system has been engaged only allowing you to travel 50mph")
    elif weatherAlert == "Blizzard":
        print("\nNational weather service has updated your alarm by 45 minutes because of the forcast of",weatherAlert)
        print("Vehicle Response system has been engaged only allowing you to travel 30mph")
    elif weatherAlert =="Rain":
        print("\nNational weather service has updated your alarm by 10 minutes because of the forcast of", weatherAlert)
        print("Vehicle Response system has been engaged only allowing you to travel 50mph")
    elif weatherAlert =="Foggy":
        print("")