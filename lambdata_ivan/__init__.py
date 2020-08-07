"""
lambdata - a collection of Data Science helper functions
"""

import pandas as pd
import numpy as np
from lambdata_ivan.dataframe_helper import report_missing_values

#Stands for DataFrameModification, This class gives you info about the df
# and cleans it from NaN's if you want.
class DFMod:
    def __init__(self,df):
        self.dataFrame = df

#this just gets all the null values into one number and prints how many there are.
#this has variation to fix english if theres only one NaN or multiple as well if they're absent!
    def nullReport(self):
        nullFound = self.dataFrame.isnull().sum().sum()
        if (nullFound == 1):
            answer1 = print('There is only', nullFound, 'NaN value in your DataFrame!')
            return answer1
        elif (nullFound > 1):
            answer2 = print('There are', nullFound, 'NaN values in your DataFrame.')
            return answer2
        else:
            print('There are no NaN values in your DataFrame!')

#Give this a list and a name and it'll turn it into a series and add it as a new column.
    def listToColumn(self, lists, name):
        newSeries =  pd.Series(lists)
        self.dataFrame[name] = newSeries
        return self.dataFrame

#This finds commonly used placeholders for NaN's and replces them to a real numpy NaN then it drops all rows containing them, cleaning the data
    def nullClean(self):
        self.dataFrame = self.dataFrame.replace({
            '?': np.nan,'nan': np.nan,'Nan':np.nan,'n/a':np.nan,
            'NaN':np.nan,' ?':np.nan,'N/A':np.nan,'na':np.nan,'NAN':np.nan
        })
        nullValue = self.dataFrame.isnull().sum().sum()
        self.dataFrame.dropna(inplace=True)
        print('There were', nullValue, "NaN's detected and removed.")
        return self.dataFrame
