def read_input() -> list[str]:
    processed_lines = []

    try:
        with open("day05/input.txt", 'r') as input_file:
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
        

def fresh_ranges(input: list[str]) -> list[int]:
    print(f"--- Start Finding FreshIDs --- \n")

    while True:
        fresh_id =  []
        for line in input:
            if line == "":
                break
            else:
                start, end = map(int, line.split('-'))
                for id in range(start, end + 1):
                    if id not in fresh_id:
                        fresh_id.append(id)
                        print(fresh_id)
        print(f" {fresh_id}  \n")
        print(f"--- FreshIDs Found --- \n")
        return fresh_id
        
def ingredients(input: list[str]) -> list[int]:
    print(f"--- Start Ingredient Function --- \n")
    ingredient_ids = []
    ingredients = False
    
    for line in input:
        if ingredients:
            ingredient_ids.append(int(line))
        elif line != "":
            continue
        else:
            ingredients = True
            continue
    
    print(f" {ingredient_ids}  \n")
    print(f"--- Ingredient IDs Found --- \n")
    return ingredient_ids

def check_freshness(fresh_ids: list[int], ingredient_ids: list[int]) -> list[int]:
    fresh_ingredients = []
    
    for ingredient in ingredient_ids:
        if ingredient in fresh_ids:
            fresh_ingredients.append(ingredient)
    
    print(f" {fresh_ingredients}  \n")
    print(f"Total Fresh Ingredients: {len(fresh_ingredients)} \n")
    print(f"--- Fresh Ingredients Found --- \n")
    return fresh_ingredients

if __name__ == "__main__":
    input = read_input()

    fresh_ids = fresh_ranges(input)
    ingredient_ids = ingredients(input)
    check_freshness(fresh_ids, ingredient_ids)
