"""Project Euler 15 - Lattice Paths"""

GRID_SIZE = 20


def main() -> None:
    lattice = [[0] * (GRID_SIZE + 1) for _ in range(GRID_SIZE + 1)]

    for edge in range(GRID_SIZE + 1):
        lattice[0][edge] = 1
        lattice[edge][0] = 1

    for row in range(1, GRID_SIZE + 1):
        for column in range(1, GRID_SIZE + 1):
            lattice[row][column] = lattice[row - 1][column] + lattice[row][column - 1]

    print(lattice[GRID_SIZE][GRID_SIZE])


if __name__ == "__main__":
    main()
