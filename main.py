# Taylor Ward
# Purpose: Create a bike class with certain properties and methods

# Import our bike class
from bike import Bike

# Instantiate a Bike object
try:
    print("=======bike1=======")
    # let's set parameters for bike1 copy of Bike
    bike1 = Bike(wheels=2, gears=15, brakes="electric", currentGear=10)
    # gears should have a min of 1 and max of 15
    print(f"gears: {bike1.getGears()}")
    # current gear should be within the range of gears
    print(f"Current gear: {bike1.getcurrentGear()}")
    # brakes should only take strings "hand brakes" or "foot brakes"
    print(f"brakes: {bike1.getBrakes()}")
    # wheels should only be 1-4
    print(f"number of wheels: {bike1.getWheels()}")

    # current gear should not go above # of gears
    # let's try to bypass the max gears by increasing current gear
    print(f"Current gear increased by 1: {bike1.incGears()}")
    print(f"Current gear increased by 1: {bike1.incGears()}")
    print(f"Current gear increased by 1: {bike1.incGears()}")
    print(f"Current gear increased by 1: {bike1.incGears()}")
    print(f"Current gear increased by 1: {bike1.incGears()}")
    print(f"Current gear increased by 1: {bike1.incGears()}")

    # reset current gear back to 1
    print(f"\nLet's reset the gears back to 1 and check it: Gear = {bike1.resetGears()}")

    # current gear should not go below 1
    # let's try to bypass the min gears
    print(f"Current gear decreased by 1: {bike1.decGears()}")

except Exception as e:
    print(f"Got an error:{e}")