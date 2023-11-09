"""
Our Welcome Screen will start our program letting
drivers know that the Infotech Center 2023 is loading
"""
#Libraries Here
import time
import sys


timeToSleep = 2

print("\nWelcome - InfoTech Center 2023")
time.sleep(timeToSleep)

#add code to have the ellipsis add a dot every .5 seconds
x = 0
ellipsis = 0

while x != 20:
    x += 1
    message = ("infoTech Center 2023 is loading" + "." * ellipsis)
    ellipsis = ellipsis + 1
    sys.stdout.write("\r" + message) # \r prints a carriage return first so message stays on same line
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis = 0
    if x ==20:
        print("\n\n Operating system loaded")

