# Properties
#  gears: getGears(), setGears()
#  currentGear: getcurrentGear(), setcurrentGear()
#  wheels: getWheels(), setWheels()
#  brakes: getBrakes()
#
# Methods
# resetGears()
# incGears()
# decGears()

class Bike:
    # Private properties
    __gears: int = 1
    __wheels: int = 2
    __currentGear: int = 1
    __brakes: str = ""
    __validBrakes = ["hand brakes", "foot brakes"]

    # Instantiate a copy of this class
    # have to put the properties with defaults at the end
    def __init__(self,
                 wheels,
                 gears,
                 brakes,
                 currentGear=1):

        # Set all of our properties
        self.setGears(gears)
        self.setWheels(wheels)
        self.setcurrentGear(currentGear)
        self.setBrakes(brakes)

    # Get and set - gears property
    def getGears(self) -> int:
        return self.__gears

    def setGears(self, gears: int) -> None:
        try:
            if 1 <= gears <= 15:
                self.__gears = int(gears)
            else:
                print(f"oops not an acceptable number of gears, setting gears to default of {self.__gears}")
        except Exception as e:
            print(f"error occurred: {e}")

    # Get and set - wheels property
    def getWheels(self) -> int:
        return self.__wheels

    def setWheels(self, wheels: int) -> None:
        try:
            if 1 <= wheels <= 4:
                self.__wheels = int(wheels)
            else:
                print(f"oops not an acceptable number of wheels, setting wheels to default of {self.__wheels}")
        except Exception as e:
            print(f"error occurred: {e}")

    # Get and set - currentGear property
    def getcurrentGear(self) -> int:
        return self.__currentGear

    def setcurrentGear(self, currentGear: int) -> None:
        try:
            if 1 <= currentGear <= 15:
                self.__currentGear = int(currentGear)
            else:
                print(f"oops currentGear is outside range of gears, setting currentGear to default of {self.__currentGear}")
        except Exception as e:
            print(f"error occurred: {e}")

    # Get and set - breaks property
    def getBrakes(self) -> str:
        return self.__brakes

    def setBrakes(self, brakes: str) -> None:
        try:
            if brakes in self.__validBrakes:
                self.__brakes = brakes
            else:
                print(f"oops not an acceptable type of breaks")
        except Exception as e:
            print(f"error occurred: {e}")

    # reset gears back to 1
    def resetGears(self) -> int:
        try:
            self.setcurrentGear(1)
            return self.getcurrentGear()
        except Exception as e:
            print(f"error occurred: {e}")

    # increase current gear by 1 (max of 15)
    def incGears(self) -> int:
        try:
            if 1 <= self.getcurrentGear() < self.getGears():
                self.setcurrentGear(self.getcurrentGear() + 1)
            else:
                print(f"oops you cannot go above {self.getGears()}")
            return self.getcurrentGear()
        except Exception as e:
            print(f"error occurred: {e}")

    # decrease current gear by 1 (min of 1)
    def decGears(self) -> int:
        try:
            if 1 < self.getcurrentGear() <= self.getGears():
                self.setcurrentGear(self.getcurrentGear() - 1)
            else:
                print("oops you cannot go below 1")
            return self.getcurrentGear()
        except Exception as e:
            print(f"error occurred: {e}")