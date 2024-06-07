import csv

def read_csv(path, delim=';'):
    with open(path, mode='r',encoding='utf-8-sig') as file:
        reader = csv.reader(file, delimiter=delim)
        return list(reader)
    
    """Mark the specified lines in the output CSV with an 'x'."""
def mark_lines(input_csv_path, input_ids_path, output_csv_path, total_lines=1000):
    # Create a list with the specified number of lines
    new_lines = [[""] for _ in range(total_lines)]
    
    # Read line numbers from the input CSV
    line_numbers = read_csv(input_csv_path)
        
    # Read the contents of the input file
    id_lines = read_csv(input_ids_path)
    lines = len(id_lines)
    
    
    # Mark the specified lines with 'x'
    for line_number in line_numbers:
        line_count = 0
        for index, id_line in enumerate(id_lines):
            if (line_number[0] == id_line[0] and (len(line_number) <= 2 or line_number[2].lower() == id_line[2].lower())):
                new_lines[index][0] = 'x'
                break;
            line_count += 1
        if (line_count >= lines):
            if (len(line_number) <= 2):
                print(line_number[1] + " not found!")
            elif (line_number[2] == ''):
                print(line_number[1] + " not found!")
            else:
                print(line_number[1] + " " + line_number[2] + " not found!")

    # Write the content to the new output CSV
    with open(output_csv_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(new_lines)
    print("done")

# Example usage
input_csv_path = 'data\\blueberry-data.csv'  # Replace with the path to your input CSV file
ids_csv_path = 'data\\input_ids.csv'  # Replace with the path to your input CSV file
output_csv_path = 'output_file.csv'   # Replace with the path to your output CSV file
mark_lines(input_csv_path, ids_csv_path, output_csv_path, 1100) 