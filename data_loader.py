import pandas as pd

class DataLoader:

   def __init__ (self, filePath):
      self.filePath = filePath

   def load(self):
       try:
          data = pd.read_parquet(self.filePath)
          print("data loaded successfully")
          return data
       except FileNotFoundError:
          print("file Not Found")
          return None
       
   def inspect(self, data):
        print("first 5 rows: ")
        print(data.head())
        print("data shape: ")
        print(data.shape)
        print("data null values: ")
        print(data.isnull().sum())
        print("data statistics: ")
        print(data.describe())

   def cleannull(self, data):
       cleanData = data.dropna(how='any')
       return cleanData