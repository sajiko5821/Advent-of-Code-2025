def read_input() -> list[str]:
    with open("day02/input.txt", "r") as input_file:
        print(" --- Read Input --- ")
        ranges = input_file.read().split(',')
        return ranges


def find_invalids_part_one(ranges: list[str]) -> int:
    print(f" --- Start Finding Invalid Ids - Part One ---")
    invalid_ids = []
    for range_str in ranges:
        start, end = map(int, range_str.split('-'))

        for id in range(start, end + 1):
            string = str(id)
            firstpart, secondpart = string[:len(string)//2], string[len(string)//2:]
            if firstpart == secondpart:
                invalid_ids.append(int(id))
    sum_invalids = sum(invalid_ids)
    print(f"Sum of invalid IDs: {sum_invalids}")
    return sum_invalids


def find_invalid_ids_part_two(ranges: list[str]) -> int:
    print(f" --- Start Finding Invalid Ids - Part Two ---")
    invalid_ids = []

    for range_str in ranges:
        start, end = map(int, range_str.split('-'))
        for id in range(start, end + 1):
            if not is_valid_id(id):
                # print(f"Invalid ID found: {id}")
                invalid_ids.append(id)

    sum_invalids = sum(invalid_ids)
    print(f"Sum of invalid IDs: {sum_invalids}")
    return sum_invalids


def is_valid_id(id: int) -> bool:
    id_string = str(id)
    total_length = len(id_string)

    # Loop over possible sequence lengths from 1 to half the total length
    for sequence_length in range(1, total_length // 2 + 1):
        # If the total length is divisible by the sequence length, check for repeating patterns.
        if total_length % sequence_length == 0:
            repetition_count = total_length // sequence_length
            base_sequence = id_string[:sequence_length]
            reconstructed_id = base_sequence * repetition_count

            if id_string == reconstructed_id:
                return False

    return True


if __name__ == "__main__":
    ranges = read_input()
    find_invalids_part_one(ranges)

    find_invalid_ids_part_two(ranges)
