import argparse
from mec.circle import mec
from mec.utils import load_points, save_output, plot_circle

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Cesta ke vstupnímu JSON souboru")
    parser.add_argument("--plot", action="store_true", help="Zobrazit vykreslení")
    args = parser.parse_args()

    points = load_points(args.input_file)
    center, radius = mec(points)
    save_output(center, radius)

    if args.plot:
        plot_circle(points, center, radius)

if __name__ == "__main__":
    main()