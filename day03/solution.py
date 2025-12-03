def read_input() -> list[str]:
    processed_lines = []

    try:
        with open("day03/input.txt", 'r') as input_file:
            print("--- Starting File Processing ---")
            for line in input_file:
                # Strip whitespace/newlines from the line
                clean_line = line.strip() 
                print(f"{clean_line}")
                processed_lines.append(clean_line)
            print("--- File Processing Complete --- \n")
            return processed_lines

    except FileNotFoundError:
        print("ERROR: The file 'input.txt' was not found. Please create it and add data.")
        return


def find_max_joltage(input: list[str]) -> int:
    print(f"--- Start Finding Max Joltage --- \n")
    total_joltage = 0

    for line in input:
        # Try all possible pairs of batteries and find the maximum
        max_value = 0

        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                # Create the number from batteries at positions i and j
                value = int(line[i] + line[j])
                if value > max_value:
                    max_value = value

        total_joltage += max_value
        print(f"Bank: {line} -> {max_value} Jolts")

    print(f"--- Finding Max Joltage Complete --- \n")
    print(f"Total Output Joltage: {total_joltage} Jolts \n")
    return total_joltage



if __name__ == "__main__":
    input = read_input()
    find_max_joltage(input)
