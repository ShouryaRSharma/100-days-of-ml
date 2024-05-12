import pandas as pd
from pathlib import Path


def load_data(dataset_name: str) -> pd.DataFrame:
    """Load a dataset from the datasets folder.

    Args:
        dataset_name: the name of the dataset

    Returns:
        a pandas DataFrame
    """
    data_path = Path(__file__).parent.parent / "datasets" / f"{dataset_name}"
    return pd.read_csv(data_path)
