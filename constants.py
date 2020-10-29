from vec3 import Vec3


ORIGIN = Vec3(0, 0, 0)

# DIST is the distance that the end effector needs to maintain from the surface.
DIST = 5.    # 5 is an arbitrary value.

# min dif values for the movement of end effector relative to its current 
# position, any disp less than these should end the algorithm
MIN_ds = Vec3(0.1, 0.1, 0.1)
MIN_dtheta = 0.1    # this could be a vector?

# steps that the manipulator takes on the path direction.
MAX_STEPS = 150         # some arbitrary number for now.

# l = distance between 2 adjacent sensors in the array
l = 5   # arbitrary value taken for now.







