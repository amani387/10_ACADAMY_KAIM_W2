import pandas as pd

def compute_top_bottom_frequent(file_path, column_name):
    # Load the dataset
    data = pd.read_csv(file_path)

    # Get top, bottom, and most frequent values
    top_10 = data[column_name].nlargest(10).tolist()
    bottom_10 = data[column_name].nsmallest(10).tolist()
    most_frequent = data[column_name].value_counts().head(10).index.tolist()

    return {"top_10": top_10, "bottom_10": bottom_10, "most_frequent": most_frequent}
