import itertools
import matplotlib.pyplot as plt
from util import City, read_cities, path_cost


def solve_tsp_dynamic(cities):
    distance_matrix = [[x.distance(y) for y in cities] for x in cities]
    cities_a = {(frozenset([0, idx + 1]), idx + 1): (dist, [0, idx + 1]) for idx, dist in
                enumerate(distance_matrix[0][1:])}
    for m in range(2, len(cities)):
        cities_b = {}
        for cities_set in [frozenset(C) | {0} for C in itertools.combinations(range(1, len(cities)), m)]:
            for j in cities_set - {0}:
                cities_b[(cities_set, j)] = min([(cities_a[(cities_set - {j}, k)][0] + distance_matrix[k][j],
                                                  cities_a[(cities_set - {j}, k)][1] + [j])
                                                 for k in cities_set if k != 0 and k != j])
        cities_a = cities_b
    res = min([(cities_a[d][0] + distance_matrix[0][d[1]], cities_a[d][1])
               for d in iter(cities_a)])
    return res[1]


if __name__ == "__main__":
    # Read cities from file
    cities = read_cities(12)

    # Solve TSP using dynamic programming
    g = solve_tsp_dynamic(cities)

    # Extract solution path
    sol = [cities[gi] for gi in g]

    # Compute the path cost
    cost = path_cost(sol)
    print(cost)

    # Visualize the solution path
    plt.scatter([c.x for c in cities], [c.y for c in cities])
    plt.title("Dynamic Programming Solution with Cost {:.2f}".format(cost))
    for i in range(len(sol)):
        plt.plot([sol[i-1].x, sol[i].x], [sol[i-1].y, sol[i].y], 'r-')
        plt.pause(2)
    plt.show(block=True)
