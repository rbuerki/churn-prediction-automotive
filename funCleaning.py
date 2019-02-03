"""
LIST OF FUNCTIONS

NaN
- nanMap: Plot heatmap with all NaN in DataFrame.
- nanList: List columns with NaN only and respective number of NaN.
- nanRemoval: Removes NaN with different strategies for selected columns. (CAUTION, simplistic approach.)

Colums
- fixDtypes: Transform datatyes of selected columns in a dataframe.
- delCols: Delete columns permanently from a dataframe.

Outliers
- outlierDetectionIQR: Detect outliers in specified columns depending on distance from 1th / 3rd quartile. NaN are ignored.
- outlierRemoval IQR: Remove outliers in specified columns depending on distance from 1th / 3rd quartile. NaN are ignored.

Transformations
- colsToLog10: Transform values of selected columns to Log10. NaN are not affected by default, parameter can be changed.

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()


# NaN

def nanMap(df, figsize=(18, 6), cmap='viridis'):
    """Plot heatmap with all NaN in DataFrame.
    Params
        ======
            df: DataFrame
            figsize: default is (18, 6)
            cmap: default is 'viridis'
    """
    plt.figure(figsize=figsize)
    sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis');


def nanList(df):
    """List columns with NaN only and respective number of NaN.
    Params
        ======
            df: DataFrame
    """
    print("Number of NaN per column:")
    for col in df:
        if df[col].isnull().sum() > 0:
            print(df[col].name +": "+str(df[col].isnull().sum()))
            

def nanRemoval(df, dropAll=False, colsToImputeNum=None, colsToImputeCat=None, colsToDrop=None):
    """Remove NaN with different strategies for selected columns. 
    Note: Use with caution, there may be better solutions in specific cases (groubed by-imputation etc.)
    Params
    ======
        df: DataFrame
        dropAll: if True ALL remaining rows with NaN will be removed, default is FALSE
        colsToImputeNumN: imputation for numeric cols, default is None
        colsToImputeCat: imputation for categorical cols, default is None
        colsToDrop: default is None
    """
    if colsToImputeNum != None:    
        for col in colsToImputeNum:
            if col in df.columns:
                display("{} - median value to impute: {}".format(col, df[col].median()))
                df[col] = df[col].fillna(df[col].median())
            else:
                display(col + " not found")
    if colsToImputeCat != None:
        for col in colsToImputeCat:
            if col in df.columns:
                display("{} - most frequent value to impute: {}".format(col, df[col].value_counts().index[0]))
                df[col] = df[col].fillna(df[col].value_counts().index[0])
            else:
                display(col + " not found")
    if colsToDrop != None:
        for col in colsToDrop:
            if col in df.columns:
                df.drop(col, axis=1, inplace=True)
            else:
                display(col + " not found")
    if dropAll:
        df = df.dropna(how='any')   # drop remaining rows with any NaNs       
    return df
    

# COLUMNS - Datatypes and Removal


def fixDtypes(df, colsToCat=None, colsToStr=None, colsToInt=None, colsToFlt=None, colsToDt=None, dtPattern="%Y/%m/%d"):
    """Transform datatyes of selected columns in a dataframe.
    Params
        ======
            df: DataFrame
            colsToCat: list of colums to category, default None
            colsToStr: list of colums to string, default None
            colsToInt: list of colums to integer, default None
            colsToFlt: list of colums to float, default None
            colsToDt: list of colums to datetime, default None
            dtPattern: datetime pattern, default = "%Y/%m/%d"
    """
    if colsToCat != None:
        for col in colsToCat:
            if col in df.columns:
                df[col] = df[col].astype('category')
            else:
                display(col + " not found")
    if colsToStr != None:
        for col in colsToStr:
            if col in df.columns:
                df[col] = df[col].astype(str)
            else:
                display(col + " not found")
    if colsToInt != None:
        for col in colsToInt:
            if col in df.columns:
                df[col] = df[col].astype(np.int64)
            else:
                display(col + " not found")
    if colsToFlt != None:
        for col in colsToFlt:
            if col in df.columns:
                df[col] = df[col].astype(np.float64)
            else:
                display(col + " not found")
    if colsToDt != None:
        for col in colsToDt:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], format=dtPattern)
            else:
                display(col + " not found")
    return df


def delCols(df, colsToDel=None):
    """Delete columns permanently from a dataframe."""
    if colsToDel != None:
        for col in colsToDel:
            if col in df.columns:
                df.drop(col, axis=1, inplace=True)
                display(col + " successfully deleted")
    return df


### OUTLIERS Detection and Removal


def outlierDetectionIQR(df, outlierCols=None, dist = 1.5):
    """Detect outliers in specified columns depending on distance from 1th / 3rd quartile. NaN are ignored.
    Params
    ======
        df: DataFrame
        outlierCols: List with columns to clean, default are all numerical columns
        dist: Cut-off distance from quartiles, default is 1.5 * IQR
    """
    outlierCols = outlierCols if outlierCols is not None else list(df.select_dtypes(include = ['float64', 'int64']).columns)
    for col in outlierCols:
        q25, q75 = np.nanpercentile(df[col], 25), np.nanpercentile(df[col], 75)
        iqr = q75 - q25
        # calculate the outlier cutoff
        cut_off = iqr * dist
        lower, upper = q25 - cut_off, q75 + cut_off
        # identify outliers
        outliers = [x for x in df[col] if x < lower or x > upper]
        print(col+'\nIdentified outliers: {}'.format(len(outliers)))
        print('Percentage of outliers: {:.1f}%\n'.format((len(outliers)/len(df[col]))*100))


def outlierRemovalIQR(df, outlierCols=None , dist = 1.5):
    """Remove outliers in specified columns depending on distance from 1th / 3rd quartile. NaN are ignored.
    Params
    ======
        df: DataFrame
        outlierCols: List with columns to clean, default are all numerical columns
        dist: Cut-off distance from quartiles, default is 1.5 * IQR
    """
    outlierCols = outlierCols if outlierCols is not None else list(df.select_dtypes(include = ['float64', 'int64']).columns)
    for col in outlierCols:
        print(col)
        length1 = len(df)
        distance = dist * (np.nanpercentile(df[col], 75) - np.nanpercentile(df[col], 25)) 
        df.drop(df[df[col] > distance + np.nanpercentile(df[col], 75)].index, inplace=True)
        df.drop(df[df[col] < np.nanpercentile(df[col], 25) - distance].index, inplace=True)
        length2 = len(df)
        print("Outliers removed: {}\n".format(length1 - length2))
    return df.copy()


### TRANSFORMATION

def colsToLog10 (df, colsToLog10, NaNTreatment=False):
    """Transform values of selected columns to Log10. NaN are not affected by default, parameter can be changed."""
    for col in df[colsToLog10]:
        df[col] = df[col].apply(lambda x: np.log10(max(x,1)))
        if NaNTreatment:
            df[col].replace(np.nan, -1, inplace=True)
        df.rename(columns={col: col+'_log'}, inplace=True)
    return df
