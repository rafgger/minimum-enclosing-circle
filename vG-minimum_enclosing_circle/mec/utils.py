import json
import numpy as np
import matplotlib.pyplot as plt

def load_points(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return [np.array([v["x"], v["y"]]) for v in data.values()]

def save_output(center, radius, file_path='output.txt'):
    with open(file_path, 'w') as f:
        f.write(f"Enclosing circle radius: {radius:.5f}\n")
        f.write(f"Enclosing circle center: {center[0]:.5f}, {center[1]:.5f}\n")

def plot_circle(points, center, radius):
    fig, ax = plt.subplots()
    xs, ys = zip(*points)
    ax.scatter(xs, ys, label='Body')
    circle = plt.Circle(center, radius, color='r', fill=False, linestyle='--', label='Minimální kruh')
    ax.add_artist(circle)
    ax.scatter(*center, color='r', label='Střed')
    ax.set_aspect('equal')
    ax.legend()
    plt.title("Minimum Enclosing Circle")
    plt.grid(True)
    plt.show()