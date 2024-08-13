import os
import json

# Path to your directory containing JSON files
json_dir = '../scraped_data'
master_json = {}

def process_all_files(json_dir):
    for filename in os.listdir(json_dir):
        if filename.endswith(".json"):
            json_file_path = os.path.join(json_dir, filename)
            print(f"Processing file: {json_file_path}")
            process_file(json_file_path)
    
    # Write the master_json dictionary to a file
    with open('../data/master_tags.json', 'w', encoding='utf-8') as outfile:
        json.dump(master_json, outfile, indent=4)

def process_file(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        title = data.get('title')
        category = data.get('category')
        content = data.get('content', {})

        if category not in master_json:
            master_json[category] = {}

        if title not in master_json[category]:
            master_json[category][title] = list(content.keys())

# Run the function to process all files and create the master JSON
process_all_files(json_dir)
