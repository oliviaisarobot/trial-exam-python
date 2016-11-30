# Create a class that represents a cuboid:
# It should take its three sizes as constructor parameters (numbers)
# It should have a method called `getSurface` that returns the cuboid's surface
# It should have a method called `getVolume` that returns the cuboid's volume

class Cuboid():
    def __init__(self, height, width, length):
        self.height = height
        self.width = width
        self.length = length

    def getSurface(self):
        return (self.height * self.width) * 2 + (self.height * self.length) * 2 + (self.width + self.length) * 2

    def getVolume(self):
        return self.height * self.width * self.length

testblock = Cuboid(2, 3, 4)
print(testblock.getSurface())
print(testblock.getVolume())
