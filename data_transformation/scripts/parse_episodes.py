import re
import pandas as pd

# Read and parse Episode Dates file
with open("The Joy Of Painting - Episode Dates", "r") as file:
    lines = file.readlines()

episode_data = []
for line in lines:
    match = re.match(r'"(.*?)" \((.*?)\)', line.strip())
    if match:
        title, date = match.groups()
        episode_data.append({"title": title, "date": pd.to_datetime(date)})

episode_df = pd.DataFrame(episode_data)

# Save the cleaned data
episode_df.to_csv("cleaned_episode_dates.csv", index=False)
