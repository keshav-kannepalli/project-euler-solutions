"""Project Euler 12 - Highly Divisible Triangular Number"""

import math


def factor_count(n: int) -> int:
    count = 0
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            count += 2 if i * i != n else 1
    return count


def triangular_number(n: int) -> int:
    return n * (n + 1) // 2


def main() -> None:
    n = 1
    while True:
        triangle = triangular_number(n)
        factors = factor_count(triangle)
        if factors > 500:
            print(triangle)
            break
        n += 1


if __name__ == "__main__":
    main()
