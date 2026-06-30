"""Project Euler 16 - Power Digit Sum"""


def main() -> None:
    digit_sum = sum(int(digit) for digit in str(2**1000))
    print(digit_sum)


if __name__ == "__main__":
    main()
