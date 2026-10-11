import csv

# Path to the 'cleaned_colors_used.csv' file
input_file = 'cleaned_colors_used.csv'
output_file = 'cleaned_colors_used_no_first_column.csv'

# Read the input file and write to the output file
with open(input_file, 'r', newline='', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    rows = list(reader)
    
    # Remove the first column from each row
    for row in rows:
        del row[0]  # Deletes the first column in each row
    
# Write the updated data to the new output file
with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(rows)

print(f"The first column has been removed and saved as '{output_file}'.")
