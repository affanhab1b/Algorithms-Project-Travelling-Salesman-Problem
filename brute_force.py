import itertools
from util import City, read_cities, path_cost
import matplotlib.pyplot as plt


class BruteForce:
    def __init__(self, cities):
        self.cities = cities

    def run(self):
        self.cities = min(itertools.permutations(self.cities),
                          key=lambda path: path_cost(path))
        return path_cost(self.cities)


if __name__ == "__main__":
    # Read cities from file
    cities = read_cities(8)

    # Create an instance of the brute force algorithm
    brute = BruteForce(cities)

    # Compute the optimal TSP tour using brute force and get the path cost
    cost = brute.run()

    # Visualize the solution path with pauses
    plt.scatter([c.x for c in cities], [c.y for c in cities])
    plt.title("Brute Force TSP Solution with Cost {:.2f}".format(cost))
    for i in range(len(brute.cities)):
        plt.plot([brute.cities[i-1].x, brute.cities[i].x],
                 [brute.cities[i-1].y, brute.cities[i].y], 'r-')
        plt.pause(1.5)
    plt.show(block=True)
