import pandas as pd

# Load the data from the CSV files
colors_df = pd.read_csv('db_colors_used.csv')
episode_df = pd.read_csv('db_episode_dates.csv')
subject_df = pd.read_csv('db_subject_matter.csv')

# Capitalize the first letter of each word in the 'title' column
colors_df['title'] = colors_df['title'].str.title()
episode_df['title'] = episode_df['title'].str.title()
subject_df['title'] = subject_df['title'].str.title()

# Save the updated data back to CSV if needed
colors_df.to_csv('updated_db_colors_used.csv', index=False)
episode_df.to_csv('updated_db_episode_dates.csv', index=False)
subject_df.to_csv('updated_db_subject_matter.csv', index=False)

print("Titles capitalized and saved.")
