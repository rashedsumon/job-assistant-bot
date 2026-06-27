import os
import glob
import pandas as pd
import kagglehub

def load_resume_dataset():
    """
    Automatically downloads the latest version of the snehaanbhawal/resume-dataset
    using kagglehub and loads the main dataset file into a Pandas DataFrame.
    """
    try:
        # Download latest version from Kaggle
        path = kagglehub.dataset_download("snehaanbhawal/resume-dataset")
        print("Path to dataset files:", path)
        
        # Search for CSV files in the downloaded path
        csv_files = glob.glob(os.path.join(path, "*.csv"))
        if csv_files:
            df = pd.read_csv(csv_files[0])
            return df, f"Successfully loaded dataset with {len(df)} records."
        else:
            return None, "Dataset downloaded, but no CSV file was found."
    except Exception as e:
        return None, f"Error downloading dataset: {str(e)}"

if __name__ == "__main__":
    # Test data loader locally
    df, message = load_resume_dataset()
    print(message)