import tabula
import pandas as pd

pdf_path = "details.pdf"

dfs = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)
print(len(dfs))
print(dfs[0].head())

data = pd.concat(dfs)
print(data.head())
print(data.shape)