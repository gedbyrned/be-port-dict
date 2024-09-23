import csv
import json

# Define the model name in the format 'app_name.ModelName'
MODEL_NAME = 'api.Word'  # Replace 'your_app_name' with the actual app name

# Input and output file paths
csv_file_path = './wordsofday.csv'  # Replace with the actual CSV file path
json_file_path = './wordsofday.json'  # Output JSON file path

# Read the CSV and convert to Django fixture format
def csv_to_django_json(csv_file_path, json_file_path):
    json_data = []
    
    with open(csv_file_path, newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)  # Read the CSV as a dictionary
        for row in reader:
            # Each row is represented as a fixture with "model" and "fields"
            json_data.append({
                "model": MODEL_NAME,  # Add the model name for Django fixtures
                "fields": {
                    "portuguese_word": row["portuguese_word"],
                    "english_word": row["english_word"],
                    "english_definition": row["english_definition"],
                }
            })
    
    # Write the JSON data to a file
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)
        
    print(f"Successfully converted {csv_file_path} to {json_file_path}")

# Run the conversion
csv_to_django_json(csv_file_path, json_file_path)
