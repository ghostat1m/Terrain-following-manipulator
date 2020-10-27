from sensor import Sensor   """will call "Sensor" class from sensor.py file"""
import numpy as np          """will import numpy library"""
import math                 """used to help in the calculation of the cosine
                               and sine angles when angle is in degrees"""

class End_eff:
    def __init__(self,transformation):
        """will be called only once throughout the whole simulation
           because just initialisation"""
        self.transformation=transformation
        """a 4x4 transformation matrix for mapping global frame and
           end-effector origin"""
        sensor_array = np.array((3, 3), dtype=Sensor)
        """defines a 3x3 array with each element a 3x1 vector for the
           xyz coordinates"""
        

    def move(self,transformation, ds):  
        """
        this move function takes as argument the class object,
        transformation matrix and 'ds' the amount of distance
        the end-effector origin should moves the end effector
        by an amount of ds

        ds: (float, float, float) a list of floats of (x, y, z) direction 
        """
        
        self.transformation[0,3]=self.transformation[0,3]+ds[0];
        """translates the end-effector origin frame in x direction"""
        self.transformation[1,3]=self.transformation[1,3]+ds[1];
        """translates the end-effector origin frame in y direction"""
        self.transformation[2,3]=self.transformation[2,3]+ds[2];
        """translates the end-effector origin frame in z direction"""
        
        return self.transformation
        """will return the updated the transformation matrix"""

    
    
    def rotate(self,transformation, dtheta):
        """
        this rotate function takes as argument the class object,
        transformation matrix and 'dtheta' the degree angles by
        which end-effector should rotate the end effector to
        assume correct orientation and update it.

        dtheta: (theta_x, theta_y, theta_z) a list of floats of (x, y, z) direction
        """
        Rotx=np.array([[0,0,0,0],[0,cosd(dtheta[0]),-sind(dtheta[0]),0],[0,sind(dtheta[0]),cosd(dtheta[0]),0],[0,0,0,1]]);
        """ x-direction roation matrix"""
        Roty=np.array([[cosd(dtheta[1]),0,-sind(dtheta[1]),0],[0,1,0,0],[sind(dtheta[1]),0,cosd(dtheta[1]),0],[0,0,0,1]]);
        """ y-direction roation matrix"""
        self.transformation=np.dot(Rotx(dtheta[0]),self.transformation)
        """ this dot product rotates the end-effector about x-axis"""
        self.transformation=np.dot(Roty(dtheta[1]),self.transformation)
        """ this dot product rotates the end-effector about y-axis"""
        
        return self.transformation
        """will return the updated the transformation matrix"""
        
    
    def dist_array(self,transformation): #this function is still incomplete because earlier we couldn't find a proper documentation on pyvista library but now we have started working on it
        """
        returns: numpy array(3x3) containing the distance to each sensor from
        the surface
        uses the pyvista library to generate surface and make a plane using the sensor points
        and find the distances using ray tracing
        """
        
        arr=np.array([[0.1,0.2,0.3], [0.4,0.5,0.6], [0.7,0.8,0.9]]); #for now we made a random distance array
        return arr                       #will return the 3x3 numpy array having distances from each of the sensor points attached on the end-effector
        
    



