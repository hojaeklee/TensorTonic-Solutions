import pandas as pd

def create_dataframe(data: dict) -> dict:
    """
    Returns a dictionary with data, shape [rows, columns], and ordered column names.
    """
    df = pd.DataFrame(data)
    data = df.to_dict(orient="list")
    shape = df.shape
    columns = df.columns
    return {
        "data": data,
        "shape": list(shape),
        "columns": list(columns)
    }
