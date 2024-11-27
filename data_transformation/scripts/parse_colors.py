import pandas as pd

# Read Colors Used file
file_path = "The Joy Of Painiting - Colors Used"
colors_df = pd.read_csv(file_path)

# Clean up strings
colors_df['colors'] = colors_df['colors'].str.replace(r"[\r\n']", "").str.strip()
colors_df['color_hex'] = colors_df['color_hex'].str.replace(r"[\r\n']", "").str.strip()

# Save the cleaned data
colors_df.to_csv("cleaned_colors_used.csv", index=False)
