import sys
from .mec import minimum_enclosing_circle
from .utils import load_points, save_result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python -m minimum_enclosing_circle <input.json>")
        sys.exit(1)
    input_path = sys.argv[1]
    points = load_points(input_path)
    center, radius = minimum_enclosing_circle(points)
    save_result(center, radius, input_path + "_result.txt")
    print(f"Enclosing circle radius: {radius:.6f}\nEnclosing circle center: {center[0]:.6f}, {center[1]:.6f}")
