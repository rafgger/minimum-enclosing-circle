import sys
from minimum_enclosing_circle.mec import minimum_enclosing_circle, plot_circle
from minimum_enclosing_circle.utils import load_points, save_result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m minimum_enclosing_circle <input.json> [--plot]")
        sys.exit(1)
    input_path = sys.argv[1]
    do_plot = len(sys.argv) > 2 and sys.argv[2] == "--plot"
    points = load_points(input_path)
    center, radius = minimum_enclosing_circle(points)
    save_result(center, radius, input_path + "_result.txt")
    print(f"Enclosing circle radius: {radius:.6f}\nEnclosing circle center: {center[0]:.6f}, {center[1]:.6f}")
    if do_plot:
        plot_circle(points, center, radius, input_path + "_circle.html")
        print(f"Vizualizace uložena do {input_path}_circle.html")
