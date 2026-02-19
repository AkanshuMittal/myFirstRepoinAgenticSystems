def read_numbers_from_file(filename):
    numbers = []
    
    with open(filename, "r") as file:
        print("File opened successfully")
        
        for line in file:
            cleaned_line = line.strip()
            
            if cleaned_line:
                number = int(cleaned_line)
                numbers.append(number)
    print(f"Read {len(numbers)} numbers")
    
    return numbers 


def statistics(numbers):
    total_count  = len(numbers)
    total_sum = sum(numbers)
    average = total_sum / total_count if total_count > 0 else 0
    
    print("Computation completed")
    
    return total_count, total_sum, average

