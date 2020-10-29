from math import sqrt

class Vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return "[{0} {1} {2}]".format(self.x, self.y, self.z)
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z

        return Vec3(x, y, z)
    
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z

        return Vec3(x, y, z)
    
    def __lt__(self, other):
        return self.norm() < other.norm()

    def __le__(self, other):
        return self.norm() <= other.norm()

    def __gt__(self, other):
        return not(self <= other)

    def __ge__(self, other):
        return not(self < other)    

    def norm(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        mag = self.norm()
        if(mag == 0):
            return 0

        return Vec3(self.x/mag, self.y/mag, self.z/mag)
