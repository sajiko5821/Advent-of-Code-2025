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


def find_max_joltage_part1(input: list[str]) -> int:
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
        # print(f"Bank: {line} -> {max_value} Jolts")

    print(f"--- Finding Max Joltage Complete --- \n")
    print(f"Total Output Joltage: {total_joltage} Jolts \n")
    return total_joltage

def find_max_joltage_part2(inputs, target_length: int) -> int:
    best = 0
    
    for line in inputs:
        length = len(line)

        # Will hold the resulting digits. Using list for stack operations.
        stack = []

        for i in range(length):
            # Pop smaller top while current digit is larger and enough digits remain for target_length.
            while len(stack) > 0 and stack[-1] < line[i] and len(stack) + (length - i) > target_length:
                stack.pop()
            
            # Add the current digit to the stack
            stack.append(line[i])

        # Ensure the resulting number is at most target_length digits long by popping from the end.
        while len(stack) > target_length:
            stack.pop()

        # print(line, stack)
        
        # Join the digits, convert to integer, and add to the running total
        best += int("".join(stack))

    print(f"--- Finding Max Joltage Complete --- \n")
    print(f"Total Output Joltage: {best} Jolts \n")
    return best


if __name__ == "__main__":
    input = read_input()
    find_max_joltage_part1(input)
    find_max_joltage_part2(input, 12)

