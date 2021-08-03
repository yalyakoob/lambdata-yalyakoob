import numpy as np
import pandas as pd


df = pd.DataFrame(np.array([[1, 2, 3], [np.nan,4, 6], [8, np.nan,9]]),
                   columns=['a', 'b', 'c'])

df1 = pd.DataFrame(np.array([[np.nan, np.nan, np.nan], [np.nan,4, 6], [8, np.nan,9]]),
                   columns=['a', 'b', 'c'])


class HelperFunctions:
    def __init__(self, dataframe):
        self.dataframe = dataframe
        #self.null_counts = null_counts

    def null_counter(self, frame):
        #df_nulls = df.isnull().sum().sum()
        #self.null_counts = df_nulls.copy()
        self.dataframe = frame
        return f'There are {frame.isnull().sum().sum()} nulls in your dataframe'

    def randomize_dataframe(self, frame):
        self.dataframe = frame
        return frame.sample(frac = 1)




'''Test'''
dataframe1 = HelperFunctions(df)
print(dataframe1.null_counter(df))
dataframe2 = HelperFunctions(df1)
print(dataframe2.null_counter(df1))
print(dataframe2.randomize_dataframe(df1))
'''Test'''
