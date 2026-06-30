"""Project Euler 17 - Number Letter Counts"""

ONES = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

TEENS = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}

TENS = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
}


def number_to_words(n: int) -> str:
    if n == 0:
        return ""

    if n < 10:
        return ONES[n]

    if n < 20:
        return TEENS[n]

    if n < 100:
        tens, ones = divmod(n, 10)
        words = TENS[tens]
        if ones:
            words += " " + ONES[ones]
        return words

    if n < 1000:
        hundreds, remainder = divmod(n, 100)
        words = ONES[hundreds] + " hundred"
        if remainder:
            words += " and " + number_to_words(remainder)
        return words

    thousands, remainder = divmod(n, 1000)
    words = number_to_words(thousands) + " thousand"
    if remainder:
        if remainder < 100:
            words += " and " + number_to_words(remainder)
        else:
            words += " " + number_to_words(remainder)
    return words


def main() -> None:
    letter_count = sum(
        len(number_to_words(n).replace(" ", "")) for n in range(1, 1001)
    )
    print(letter_count)


if __name__ == "__main__":
    main()
