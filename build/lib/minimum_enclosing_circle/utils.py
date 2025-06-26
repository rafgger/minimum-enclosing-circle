import json
from typing import List, Tuple

Point = Tuple[float, float]

def load_points(json_path: str) -> List[Point]:
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    points = []
    for v in data.values():
        x = float(str(v['x']).replace(' ', '').replace(',', '.'))
        y = float(str(v['y']).replace(' ', '').replace(',', '.'))
        points.append((x, y))
    return points

def save_result(center: Point, radius: float, out_path: str):
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(f"Enclosing circle radius: {radius:.6f}\n")
        f.write(f"Enclosing circle center: {center[0]:.6f}, {center[1]:.6f}\n")
