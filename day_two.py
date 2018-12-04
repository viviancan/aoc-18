import collections
from operator import itemgetter


def main():
    print("day two advent!")

    test_input_list = ["abcdef", "bababc", "abbcde",
                       "abcccd", "aabcdd", "abcdee", "ababab"]

    test_input_two = ["abcde",
                      "fghij",
                      "klmno",
                      "pqrst",
                      "fguij",
                      "axcye",
                      "wvxyz"]
    two_count = 0
    three_count = 0

    with open("day_two_input.txt", "r") as f:
        for string in f:
            character_count = collections.defaultdict(int)

            for c in string:
                character_count[c] += 1

            values = character_count.values()

            if 2 in values and 3 in values:
                two_count += 1
                three_count += 1
            elif 2 in values:
                two_count += 1
            elif 3 in values:
                three_count += 1

        checksumm = two_count * three_count
        print(checksumm)
        # Answer = 5928


if __name__ == '__main__':
    main()
