from vec3 import Vec3
import pyvista as pv
import numpy as np
'''distance valuse assumed in meters'''

class Sensor:
    def __init__(self, x, y, z):
        # relative_pos = Vec3(x, y, 0)     # position relative to end effectors origin
        # global_pos =          [TODO]
        pass
    
    def dist(self, surface, direction,range_of_sensor=10):
        """
        computes distance of the sensor from the surface in the direction of the
        z-axis of the end effector using Ray marching algorithm.
        
        returns: (float) distance of the sensor from the surface.

        surface: is the representation of the surface [TODO]
        direction: (Vec3) z axis of the end effector wrt Global Coordinates.
        """
        rayOrigin=np.array([self.x,self.y,self.z])
        rayEnd=rayOrigin+range_of_sensor*direction
        ip,ic=surface.ray_trace(rayOrigin,rayEnd,first_point=True)
        if not ip:#check if intersection point array is empty sinifying no intersection found
        	print('no intersection found')
        	dist= 10000
        else:	
        	distance=np.sqrt(np.sum(ip-rayOrigin))#ip in the intersection point
        	
        return distance
   
    def update_pos(self, dx, dy, dz):
        """
        updates the global position of the sensors.

        dx = (float) disp in global x direction
        dy = (float) disp in global y direction
        dz = (float) disp in global z direction
        """
        pass


    
