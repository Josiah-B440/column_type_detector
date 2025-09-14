import pandas as pd

def detect_column_types(df: pd.DataFrame, cat_threshold: int = 20) -> dict:
    
    column_types = {}

    for col in df.columns:
        series = df[col]
        dtype = series.dtype

        if pd.api.types.is_numeric_dtype(dtype):
            if series.nunique() <= cat_threshold:
                column_types[col] = "categorical"
            else:
                column_types[col] = "numerical"

        elif pd.api.types.is_string_dtype(dtype):
            if series.nunique() <= cat_threshold:
                column_types[col] = "categorical"
            else:
                column_types[col] = "text"

        else:
            column_types[col] = "categorical"

    return column_types
