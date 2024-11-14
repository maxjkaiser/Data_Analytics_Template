# utils.py

def clean_data(df):
    """Clean the dataset by removing missing values and duplicates."""
    df = df.dropna()
    df = df.drop_duplicates()
    return df
