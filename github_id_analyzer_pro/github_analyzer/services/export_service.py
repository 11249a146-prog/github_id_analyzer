from io import BytesIO
import pandas as pd

def dataframe_to_csv(df):
    return df.to_csv(index=False).encode("utf-8")

def dataframe_to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Repositories")
    return output.getvalue()
