# from end_effector import End_eff
from constants import l, DIST
from vec3 import Vec3
import math

def rot_matrix(M, theta):
    """
    returns a 3x3 rotation matrix
    M is a Vec3 vector about which the frame has to be rotated
    theta is the angle by which the frame would be rotated
    """

    m = M.normalize()
    s = math.sin(theta)
    c = math.cos(theta)
    v = 1-c

    row1 = [
        (m.x)**2 * v + c,
        m.x*m.y*v - m.z*s,
        m.x*m.z*v + m.y*s
    ]
    
    row2 = [
        m.x*m.y*v + m.z*s, 
        m.y**2 * v + c,
        m.y*m.z*v - m.x*s
    ]

    row3 = [
        m.x*m.z*v - m.y*s,
        m.y*m.z*v + m.x*s, 
        m.z**2*v + c
    ]
    rot_mat = [row1, row2, row3]

    return rot_mat


def coordinate_mat(dist_mat):
    # mat = [
    #     [Vec3(-l, l, dist_mat[0][0]), Vec3(0, l, dist_mat[0][1]), Vec3(l, l, dist_mat[0][2])]
    #     [Vec3(-l, 0, dist_mat[1][0]), Vec3(0, l, dist_mat[1][1]), Vec3(l, 0, dist_mat[1][2])]
    #     [Vec3(-l, -l, dist_mat[2][0]), Vec3(0, -l, dist_mat[2][1]), Vec3(l, -l, dist_mat[2][2])]
    # ]

    rows = 3
    cols = 3

    mat = [[0 for x in range(rows) for y in range(cols)]]

    start_y = -l
    for i in range(rows):
        start_x = -l
        for j in range(cols):
            mat[i][j] = Vec3(start_x, start_y, dist_mat[i][j])
            start_x += l

        start_y += l

    return mat


def best_fit_plane(co_mat):
    a_coef = 0
    b_coef = 0
    a_rval = 0
    b_rval = 0
    c_coef = 0
    c_rval = 0

    for i in range(3):
        for j in range(3):
            a_coef += (co_mat[i][j].x)**2
            b_coef += (co_mat[i][j].y)**2
            c_coef -= 1
            a_rval -= (co_mat[i][j].x)*(co_mat[i][j].z)
            b_rval -= (co_mat[i][j].y)*(co_mat[i][j].z)
            c_rval -= (co_mat[i][j].z)

    a = a_rval/a_coef
    b = b_rval/b_coef
    c = c_rval/c_coef

    return (a, b, c)


def orientation(co_mat):
    """
    returns: vec3 object, a vec3 about which end eff has to be rotated.

    co_mat: coordinate matrix formed from dist mat.
    """

    a, b, c = best_fit_plane(co_mat)

    M = Vec3(-b, a, 0)
    theta = math.acos(1/math.sqrt(a**2 + b**2 + 1))

    return rot_matrix(M, theta)


def closest_point(co_mat):
    """
    returns: vec3 point closest to the end effector by first creating a surface 
    from the points using dist_mat and then running a minimizing algo like 
    hookes and jeeves method to find the minima

    but for now it simply returns the point with minimum z in the dist_mat
    """
   
    for i in min_co:
        for j in i:
            if min_co.z > j.z:
                min_co = j

    return min_co


def algo(dist_mat):
    """
    returns new orientation and new position of the origin( to be considered as a displacement vector)
    dist_mat is the distance matrix returned by the end effector after taking the readings from the sensors.
    """

    or_mat = orientation(dist_mat)
    p_min = closest_point(dist_mat)

    co_mat = coordinate_mat(dist_mat)
    v_sum = Vec3(0, 0, 0)
    count = 0
    for i in co_mat:
        for j in i:
            v_sum = v_sum + j
            count += 1

    centroid = Vec3(v_sum.x/count, v_sum.y/count, v_sum.z/count)

    a, b, c = best_fit_plane(co_mat)
    new_z = DIST + p_min.z - c + a * p_min.x + b * p_min.y
    P_new = centroid - Vec3(0, 0, new_z)

    return or_mat, P_new
