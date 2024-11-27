import pandas as pd

subject_file = "The Joy Of Painting - Subject Matter"
subject_df = pd.read_csv(subject_file)

# Normalize boolean columns (optional)
bool_columns = subject_df.columns[2:]  # Assuming 3rd column onwards are boolean
subject_df[bool_columns] = subject_df[bool_columns].astype(bool)

# Save the cleaned data
subject_df.to_csv("cleaned_subject_matter.csv", index=False)
