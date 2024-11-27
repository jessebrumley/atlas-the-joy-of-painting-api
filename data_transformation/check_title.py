import pandas as pd

def check_title_matching(subject_matter_file, colors_used_file, episode_dates_file):
    # Read in the data
    subject_matter_df = pd.read_csv(subject_matter_file)
    colors_df = pd.read_csv(colors_used_file)
    episode_df = pd.read_csv(episode_dates_file)

    # Normalize 'Title' columns by stripping spaces and converting to lowercase for all three dataframes
    subject_matter_df['Title'] = subject_matter_df['Title'].str.strip().str.lower()
    colors_df['Title'] = colors_df['Title'].str.strip().str.lower()
    episode_df['Title'] = episode_df['Title'].str.strip().str.lower()

    # Find titles in subject_matter that are not in colors_used
    subject_not_in_colors = subject_matter_df[~subject_matter_df['Title'].isin(colors_df['Title'])]
    colors_not_in_subject = colors_df[~colors_df['Title'].isin(subject_matter_df['Title'])]

    # Find titles in subject_matter that are not in episode_dates
    subject_not_in_episode = subject_matter_df[~subject_matter_df['Title'].isin(episode_df['Title'])]
    episode_not_in_subject = episode_df[~episode_df['Title'].isin(subject_matter_df['Title'])]

    # Find titles in colors_used that are not in episode_dates
    colors_not_in_episode = colors_df[~colors_df['Title'].isin(episode_df['Title'])]
    episode_not_in_colors = episode_df[~episode_df['Title'].isin(colors_df['Title'])]

    # Output results showing full rows where mismatches happen

    print("\nRows in subject_matter but not in colors_used:")
    print(subject_not_in_colors)
    print("\nRows in colors_used but not in subject_matter:")
    print(colors_not_in_subject)
    
    print("\nRows in subject_matter but not in episode_dates:")
    print(subject_not_in_episode)
    print("\nRows in episode_dates but not in subject_matter:")
    print(episode_not_in_subject)

    print("\nRows in colors_used but not in episode_dates:")
    print(colors_not_in_episode)
    print("\nRows in episode_dates but not in colors_used:")
    print(episode_not_in_colors)


def main():
    # File paths
    subject_matter_file = 'db_subject_matter.csv'
    colors_used_file = 'db_colors_used.csv'
    episode_dates_file = 'db_episode_dates.csv'

    # Check title matching across the files
    check_title_matching(subject_matter_file, colors_used_file, episode_dates_file)

if __name__ == "__main__":
    main()
