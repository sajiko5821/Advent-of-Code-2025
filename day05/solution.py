def read_input() -> list[str]:
    print("--- Reading Input ---")
    with open("day05/input.txt", 'r') as input_file:
        processed_lines = []
        for line in input_file:
            # Strip whitespace from the line
            clean_line = line.strip() 
            print(f"{clean_line}")
            processed_lines.append(clean_line)
    print("--- Input Reading Complete --- \n")
    return processed_lines


def process_input(input: list[str]) -> tuple[list[range], list[int]]:
    print("--- Starting Input Processing ---")
    ranges = []
    ids = []
    for line in input:
        if "-" in line:
            (a, b) = line.split('-')
            ranges.append(range(int(a), int(b) + 1))
        elif line != "":
            ids.append(int(line))

    ranges.sort(key=lambda r: (r.start, r.stop))
    i = 0
    while i < len(ranges):
        range1 = ranges[i]
        j = i + 1
        while j < len(ranges):
            range2 = ranges[j]
            if range2.start <= range1.stop:
                range1 = range(range1.start, max(range1.stop, range2.stop))
                ranges[i] = range1
                del ranges[j]
            else:
                break
        i += 1

    print("--- Input Processing Complete --- \n")
    return ranges, ids


def part1(ranges: list[range], ids: list[int]) -> int:
    """Count how many `ids` are contained in any of the `ranges`."""
    print("--- Starting Part 1 Calculation ---")
    count = 0
    for value in ids:
        # Check if this value falls into ANY of the merged ranges.
        if any(value in r for r in ranges):
            count += 1

    print(f"Part 1 Result: {count}")
    print("--- Part 1 Calculation Complete --- \n")
    return count


if __name__ == "__main__":
    input = read_input()
    ranges, ids = process_input(input)
    part1(ranges, ids)
