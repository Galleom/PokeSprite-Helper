import csv
import json

def csv_to_json_no_keys(csv_file_path, json_file_path):
    # Read the CSV and add data to a list of lists
    data = []
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            print(row[0].split(";"))
            data.append(row[0].split(";"))

    # Write the list of lists to a JSON file
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file)

# Example usage
csv_file_path = '.\\pokedata\\table_pokedata.csv'  # Replace with your CSV file path
json_file_path = 'output.json'  # Replace with your desired JSON file path
csv_to_json_no_keys(csv_file_path, json_file_path)

print(f"CSV file {csv_file_path} has been converted to JSON file {json_file_path}.")
