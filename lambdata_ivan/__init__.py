
"""
lambdata - a collection of Data Science helper functions
"""

import pandas as pd
import numpy as np
from lambdata_ivan.dataframe_helper import report_missing_values


def nullReport(df):
    df.copy
    nullFound = df.isnull().sum().sum()
    if (nullFound == 1):
        answer1 = print('There is only', nullFound, 'NaN value in your DataFrame!')
        return answer1
    elif (nullFound > 1): 
        answer2 = print('There are', nullFound, 'NaN values in your DataFrame.')
        return answer2
    else:
        print('There are no NaN values in your DataFrame!')


def listToColumn(df, lists,name):
    lists.copy
    df.copy
    newSeries =  pd.Series(lists)
    df[name] = newSeries
    return df

