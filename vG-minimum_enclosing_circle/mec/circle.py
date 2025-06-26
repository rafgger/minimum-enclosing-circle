import numpy as np
import random

def dist(p1, p2):
    return np.linalg.norm(p1 - p2)

def circle_from(p1, p2, p3=None):
    if p3 is None:
        center = (p1 + p2) / 2
        radius = dist(p1, p2) / 2
    else:
        A = np.linalg.det([
            [p1[0], p1[1], 1],
            [p2[0], p2[1], 1],
            [p3[0], p3[1], 1]
        ])
        if abs(A) < 1e-10:
            return None
        D = 2 * np.linalg.det([
            [p1[0], p1[1], 1],
            [p2[0], p2[1], 1],
            [p3[0], p3[1], 1]
        ])
        Ux = np.linalg.det([
            [p1[0]**2 + p1[1]**2, p1[1], 1],
            [p2[0]**2 + p2[1]**2, p2[1], 1],
            [p3[0]**2 + p3[1]**2, p3[1], 1]
        ]) / D
        Uy = np.linalg.det([
            [p1[0], p1[0]**2 + p1[1]**2, 1],
            [p2[0], p2[0]**2 + p2[1]**2, 1],
            [p3[0], p3[0]**2 + p3[1]**2, 1]
        ]) / D
        center = np.array([Ux, Uy])
        radius = dist(center, p1)
    return center, radius

def is_in_circle(p, center, radius):
    return dist(p, center) <= radius + 1e-8

def mec(points):
    def welzl(P, R):
        if len(P) == 0 or len(R) == 3:
            if len(R) == 0:
                return np.array([0.0, 0.0]), 0.0
            elif len(R) == 1:
                return R[0], 0.0
            elif len(R) == 2:
                return circle_from(R[0], R[1])
            else:
                return circle_from(R[0], R[1], R[2])

        p = P.pop()
        c, r = welzl(P, R)
        if is_in_circle(p, c, r):
            P.append(p)
            return c, r
        else:
            R.append(p)
            c2, r2 = welzl(P, R)
            P.append(p)
            R.pop()
            return c2, r2

    P = points[:]
    random.shuffle(P)
    return welzl(P, [])