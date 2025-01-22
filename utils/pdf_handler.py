import tabula
import pandas as pd


class PDFHandler:
  
    def extract_data(self, pdf_path):
        dfs = tabula.read_pdf(pdf_path, pages='all')
        main_df = dfs[0]
        for df in dfs[1:]:
            mail = df.columns
            df = df.rename(columns={mail[0]: 'Company Name',mail[1]: 'Email ID', mail[2]: mail[2]})
            df.loc[len(df)] = mail
            main_df = pd.concat([main_df, df])
        return main_df[['Company Name', 'Email ID']]
    
    def save_data(self, data):
        data.to_csv("data.csv", index=False)
    
    def __call__(self, pdf_path):
        data = self.extract_data(pdf_path)
        self.save_data(data)
        return data


if __name__ == "__main__":
    pdf_handler = PDFHandler()
    data = pdf_handler("details.pdf")
    print(data.head())
    print(data.shape)