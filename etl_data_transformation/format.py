import csv

# Input file path (will overwrite the original file)
file_path = 'db_colors_used.csv'

# Read the input CSV and rearrange the columns
with open(file_path, mode='r', newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    
    # Define the new order of columns
    fieldnames = reader.fieldnames
    episode_index = fieldnames.index('Episode')
    title_index = fieldnames.index('Title')

    # Ensure Title column comes right after Episode column
    new_fieldnames = fieldnames[:episode_index + 1] + ['Title'] + fieldnames[episode_index + 1:title_index] + fieldnames[title_index + 1:]

    # Read the rows and write them to the same file with the new column order
    rows = [row for row in reader]

with open(file_path, mode='w', newline='', encoding='utf-8') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=new_fieldnames)
    writer.writeheader()
    
    # Write each row with the new column order
    for row in rows:
        reordered_row = {key: row[key] for key in new_fieldnames}
        writer.writerow(reordered_row)

print(f"CSV file '{file_path}' has been modified and saved.")
