def read_input() -> list[str]:
    with open("day02/input.txt", "r") as input_file:
        print(" --- Read Input --- ")
        ranges = input_file.read().split(',')
        return ranges


def find_duplicates(ranges: list[str]) -> list[int]:
    print(f" --- Start Finding Duplicates ---")

    for range_str in ranges:
        start, end = map(int, range_str.split('-'))
        # print(f"Processing range: {start}-{end}")

        for id in range(start, end + 1):
            string = str(id)
            firstpart, secondpart = string[:len(string)//2], string[len(string)//2:]
            if firstpart == secondpart:
                invalid_ids.append(int(id))
                # print(f"Invalid: {string}")


if __name__ == "__main__":
    invalid_ids = []

    ranges = read_input()
    find_duplicates(ranges)
    sum_invalid = sum(invalid_ids)
    print(f"Sum of invalid IDs: {sum_invalid}")
