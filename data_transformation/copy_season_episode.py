import pandas as pd

def standardize_episode_column(df, subject_df, column_name='episode'):
    """
    Standardize the episode column to ensure consistent formatting and match 
    the episode values from the subject_df.
    """
    # Copy the episode column from subject_df to df to ensure consistency row by row
    df[column_name] = subject_df[column_name]
    
    # Ensure the episode is stripped of extra spaces or quotes
    df[column_name] = df[column_name].apply(lambda x: str(x).strip())
    
    return df

def merge_datasets(colors_file, episode_file, subject_file, output_file):
    # Load the CSV files into DataFrames
    colors_df = pd.read_csv(colors_file)
    episode_df = pd.read_csv(episode_file)
    subject_df = pd.read_csv(subject_file)
    
    # Standardize the 'episode' column in all DataFrames
    colors_df = standardize_episode_column(colors_df, subject_df)
    episode_df = standardize_episode_column(episode_df, subject_df)
    subject_df = standardize_episode_column(subject_df, subject_df)  # This will ensure consistency
    
    # Merge the DataFrames on the 'episode' column
    merged_df = colors_df.merge(episode_df, on='episode', how='left')
    merged_df = merged_df.merge(subject_df, on='episode', how='left')
    
    # Save the merged DataFrame to a new CSV file
    merged_df.to_csv(output_file, index=False)
    print(f"Merged dataset saved to {output_file}")

def main():
    # File paths for the 3 CSV files
    colors_file = 'db_colors_used.csv'
    episode_file = 'db_episode_dates.csv'
    subject_file = 'db_subject_matter.csv'
    
    # Output file path for the merged dataset
    output_file = 'merged_painting_data.csv'
    
    # Merge the datasets
    merge_datasets(colors_file, episode_file, subject_file, output_file)

if __name__ == "__main__":
    main()
