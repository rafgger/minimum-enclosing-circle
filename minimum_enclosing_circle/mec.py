import numpy as np
from typing import List, Tuple, Optional
from minimum_enclosing_circle.utils import Point
import random
import plotly.graph_objects as go

# Checks if a point lies inside or on the boundary of a given circle.
def is_in_circle(p: Point, c: Point, r: float) -> bool:
    return bool(np.linalg.norm(np.array(p) - np.array(c)) <= r + 1e-10)

# Computes the unique circle passing through two or three points. 
# For two points, it returns the circle with the segment as diameter. 
# For three, it solves for the circumcircle. If the points are colinear, 
# it returns the circle defined by the two farthest points.
def circle_from(p1: Point, p2: Point, p3: Optional[Point] = None) -> Tuple[Point, float]:
    if p3 is None:
        center = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
        radius = float(np.linalg.norm(np.array(p1) - np.array(center)))
        return center, radius
    A = np.array([[p2[0] - p1[0], p2[1] - p1[1]], [p3[0] - p1[0], p3[1] - p1[1]]])
    B = np.array([
        ((p2[0] ** 2 - p1[0] ** 2) + (p2[1] ** 2 - p1[1] ** 2)) / 2,
        ((p3[0] ** 2 - p1[0] ** 2) + (p3[1] ** 2 - p1[1] ** 2)) / 2
    ])
    try:
        sol = np.linalg.solve(A.T, B)
        center = (sol[0] + p1[0], sol[1] + p1[1])
        radius = float(np.linalg.norm(np.array(center) - np.array(p1)))
        return center, radius
    except np.linalg.LinAlgError:
        # Points are colinear
        pairs = [(p1, p2), (p1, p3), (p2, p3)]
        dists = [np.linalg.norm(np.array(a) - np.array(b)) for a, b in pairs]
        i = int(np.argmax(dists))
        a, b = pairs[i]
        return circle_from(a, b)

# Implements Welzl’s recursive algorithm. 
# It builds the minimum enclosing circle by recursively 
# considering points and a boundary set (at most 3 points). 
# If a point is not inside the current circle, it is added to the boundary.
def mec(points: List[Point], boundary: List[Point] = []) -> Tuple[Point, float]:
    if len(points) == 0 or len(boundary) == 3:
        if len(boundary) == 0:
            return ((0, 0), 0)
        elif len(boundary) == 1:
            return (boundary[0], 0)
        elif len(boundary) == 2:
            return circle_from(boundary[0], boundary[1])
        else:
            return circle_from(boundary[0], boundary[1], boundary[2])
    p = points.pop()
    c, r = mec(points, boundary)
    if is_in_circle(p, c, r):
        points.append(p)
        return c, r
    else:
        boundary.append(p)
        res = mec(points, boundary)
        boundary.pop()
        points.append(p)
        return res

# Shuffles the input points and calls mec to compute the MEC.
def minimum_enclosing_circle(points: List[Point]) -> Tuple[Point, float]:
    pts = points[:]
    random.shuffle(pts)
    center, radius = mec(pts, [])
    return center, radius

# Uses Plotly to visualize the points, the enclosing circle, and its center.
def plot_circle(points: List[Point], center: Point, radius: float, out_path: Optional[str] = None):
    xs, ys = zip(*points)
    fig = go.Figure()
    # Body
    fig.add_trace(go.Scatter(x=xs, y=ys, mode='markers', name='Body', marker=dict(size=8)))
    # Kruh
    theta = np.linspace(0, 2 * np.pi, 200)
    circle_x = center[0] + radius * np.cos(theta)
    circle_y = center[1] + radius * np.sin(theta)
    fig.add_trace(go.Scatter(x=circle_x, y=circle_y, mode='lines', name='Opsaný kruh'))
    # Střed
    fig.add_trace(go.Scatter(x=[center[0]], y=[center[1]], mode='markers', name='Střed', marker=dict(size=12, color='red', symbol='x')))
    fig.update_layout(title='Minimum Enclosing Circle', xaxis_title='x', yaxis_title='y', yaxis_scaleanchor='x', yaxis_scaleratio=1)
    if out_path:
        fig.write_html(out_path)
    else:
        fig.show()

from minimum_enclosing_circle.utils import load_points, save_result
