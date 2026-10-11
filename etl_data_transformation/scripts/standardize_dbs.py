import pandas as pd
import re

# Load the files
colors_df = pd.read_csv("db_colors_used.csv")
dates_df = pd.read_csv("db_episode_dates.csv")
subjects_df = pd.read_csv("db_subject_matter.csv")

# Standardize Dates
dates_df['date'] = pd.to_datetime(dates_df['date'], errors='coerce').dt.strftime('%Y-%m-%d')

# Standardize Titles
title_mapping = dates_df.set_index('title')['date'].to_dict()
colors_df['painting_title'] = colors_df['painting_title'].map(title_mapping).fillna(colors_df['painting_title'])
subjects_df['painting_title'] = subjects_df['painting_title'].map(title_mapping).fillna(subjects_df['painting_title'])

# Normalize Color Names
def normalize_colors(color_list):
    color_list = re.sub(r"[\[\]'\"\r\n]", "", color_list)  # Remove brackets, quotes, and extra characters
    return [color.strip().lower().replace(" ", "_") for color in color_list.split(",")]

colors_df['colors'] = colors_df['colors'].apply(normalize_colors)
colors_df['color_hex'] = colors_df['color_hex'].apply(normalize_colors)

# Normalize Subject Matter
def normalize_subject(subject):
    return subject.strip().lower().replace(" ", "_")

subject_columns = subjects_df.columns[1:]  # Skip the ID or episode column
for col in subject_columns:
    subjects_df[col] = subjects_df[col].apply(normalize_subject)

# Save Updated Files
colors_df.to_csv("final_colors_used.csv", index=False)
dates_df.to_csv("final_episode_dates.csv", index=False)
subjects_df.to_csv("final_subject_matter.csv", index=False)

print("Standardization complete.")
