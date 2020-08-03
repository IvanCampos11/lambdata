"""
lambdata - a collection of Data Science helper functions
"""

import pandas as pd
import numpy as np
from lambdata_ivan.dataframe_helper import report_missing_values


def nullReport(df):
    df.copy
    nullFound = df.isnull().sum().sum()
    answer = print('There is', nullFound,'NaN values in your DataFrame.')
    return answer

def listToColumn(df, lists):
    lists.copy
    df.copy
    newSeries =  pd.Series(list)
    df['New Column'] = newSeries
    return df

