import csv

def read_csv(path, delim=';'):
    with open(path, mode='r',encoding='utf-8-sig') as file:
        reader = csv.reader(file, delimiter=delim)
        return list(reader)
    
    """Mark the specified lines in the output CSV with an 'x'."""
def find_ids(input_ids_path, output_path):
        
    # Read the contents of the input file
    id_lines = read_csv(input_ids_path)
    lines = []
    gen = 0;
    first_gen_dex_ids = [
        1,
        152,
        252,
        387,
        494,
        650,
        722,
        810,
        906
    ]
    for index, id_line in enumerate(id_lines):
        if (int(id_line[0]) == first_gen_dex_ids[gen]):
            lines.append(index)
            gen += 1
            if (gen == len(first_gen_dex_ids)):
                break;

    lines.append(len(id_lines) - 1)
    # Write the content to the new output CSV
    with open(output_path, mode='w') as file:
        for index, line in enumerate(lines):
            file.write(str(index+1) + ": " + str(line) + ",")
            print(str(index+1) + ": " + str(line) + ",")
    print("done")

# Example usage
ids_csv_path = 'data\\input_ids.csv'  # Replace with the path to your input CSV file
output_path = 'output_file.txt'   # Replace with the path to your output CSV file
find_ids(ids_csv_path, output_path) 