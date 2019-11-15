import time
import sys
import os

def loadingscreen():
    toolbar_width = 60
    print("Loading......")
    # setup toolbar
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

    for i in xrange(toolbar_width):
        time.sleep(0.2) # do real work here
        # update the bar
        sys.stdout.write("*")
        sys.stdout.flush()

    sys.stdout.write("]\n") # this ends the progress bar
loadingscreen()

if raw_input("Are you sure? (Y/N) [Use UPPER-CASE letters]") != "y":
    os.system('cls' if os.name == 'nt' else 'clear')
    testgrade = raw_input("What did you get on your test? [Numbers only 1234567890]")
    if testgrade == "50":
        print("You have met expetations")
    if testgrade < "50":
        print("YOU HAVE FAILED YOUR TEST!")
    if testgrade > "50":
        print("You have passed your test!")
