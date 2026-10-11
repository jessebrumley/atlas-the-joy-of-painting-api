import csv
from collections import defaultdict

# Path to the CSV file
csv_file = 'db_subject_matter.csv'

# Initialize a defaultdict to store titles and their line numbers
titles = defaultdict(list)

# Read the CSV file and extract titles
with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for line_number, row in enumerate(reader, start=1):
        title = row['Title']
        titles[title].append(line_number)

# Check for duplicates and display them
duplicates = {title: lines for title, lines in titles.items() if len(lines) > 1}

if duplicates:
    print("Duplicate Titles:")
    for title, lines in duplicates.items():
        print(f"Title: {title}")
        print(f"Duplicate lines: {', '.join(map(str, lines))}")
else:
    print("No duplicates found.")
