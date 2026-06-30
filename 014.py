"""Project Euler 14 - Longest Collatz Sequence"""

LIMIT = 1_000_000


def collatz_chain_length(n: int, cache: dict[int, int]) -> int:
    if n in cache:
        return cache[n]

    if n == 1:
        return 1

    if n % 2 == 0:
        length = 1 + collatz_chain_length(n // 2, cache)
    else:
        length = 1 + collatz_chain_length(3 * n + 1, cache)

    cache[n] = length
    return length


def main() -> None:
    cache: dict[int, int] = {1: 1}
    best_start = 0
    best_length = 0

    for start in range(2, LIMIT):
        length = collatz_chain_length(start, cache)
        if length > best_length:
            best_length = length
            best_start = start

    print(best_start)


if __name__ == "__main__":
    main()
