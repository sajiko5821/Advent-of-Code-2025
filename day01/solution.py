def read_input():
    # List to store processed lines
    processed_lines = [] 

    try:
        with open("day01/input.txt", 'r') as input_file:
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

def turn_dial_1(input, dialsize, dial_position, count_dial_at_zero):
    print(f"--- Start Dial Rotation ---")
    for line in input:
        try:
            # Split the input line into direction and amount
            direction = line[0]
            amount_str = line[1:]
            
            amount = int(amount_str)
        except (IndexError, ValueError):
            print(f"Skipping malformed input: {line}")
            continue

        # Update the dial position based on direction
        if direction == "R":
            dial_position = (dial_position + amount) % dialsize
        elif direction == "L":
            dial_position = (dial_position - amount) % dialsize
        else:
            print(f"Unknown direction: {direction}. Skipping step.")
            continue
        
        # Check if the dial landed exactly on the zero position
        if dial_position == 0:
            count_dial_at_zero += 1
        
        # print(f"Step: {line:<4} | New Position: {dial_position:<3} | Times at Zero: {count_dial_at_zero}")
    print(f"Final Position: {dial_position:<3} | Times at Zero: {count_dial_at_zero}")
    print(f"--- Dial Rotation Complete --- \n")
    
    return dial_position, count_dial_at_zero
    

def turn_dial_2(input, dialsize, dial_position, count_zero_tick):
    print(f"--- Start Dial Rotation ---")
    for line in input:
        try:
            # Split the input line into direction and amount
            direction = line[0]
            amount_str = line[1:]
            
            amount = int(amount_str)
        except (IndexError, ValueError):
            print(f"Skipping malformed input: {line}")
            continue

        # Update the dial position based on direction
        if direction == "R":
            for _ in range(amount):
                dial_position = (dial_position + 1) % dialsize
                if dial_position == 0:
                    count_zero_tick += 1
        elif direction == "L":
            for _ in range(amount):
                dial_position = (dial_position - 1) % dialsize
                if dial_position == 0:
                    count_zero_tick += 1
        else:
            print(f"Unknown direction: {direction}. Skipping step.")
            continue
        
        # print(f"Step: {line:<4} | New Position: {dial_position:<3} | Zero Ticks: {count_zero_tick}")
    print(f"Final Position: {dial_position:<3} | Zero Ticks: {count_zero_tick}")
    print(f"--- Dial Rotation Complete ---")
    
    return dial_position, count_zero_tick
    
if __name__ == "__main__":
    # Initialize variables
    dialsize = 100
    dial_position=50
    count_dial_at_zero = 0
    count_zero_tick = 0
    
    input = read_input()
    turn_dial_1(input, dialsize, dial_position, count_dial_at_zero)
    turn_dial_2(input, dialsize, dial_position, count_zero_tick)