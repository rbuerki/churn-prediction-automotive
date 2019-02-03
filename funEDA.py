import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set_style('whitegrid')
from tqdm import tqdm


# Plots of numerical features

def histDF(df, figsize=(16, 16), bins=50, color='rebeccapurple'):
    """Plots histograms for all numerical columns in DataFrame.
    Params
        ======
            df: DataFrame
            figsize: default is (16, 16)
            bins: default is 50
            color: default is 'rebeccapurple'
    """
    df_num = df.select_dtypes(include = ['float64', 'int64'])
    df_num.hist(figsize=figsize, bins=bins, xlabelsize=8, ylabelsize=8, color=color);
    return df_num


def boxplotDF(df, figsize=(16, 16), color='rebeccapurple'):
    """Plots boxplots for all numerical columns in DataFrame.
    Params
    ======
        df: DataFrame
        figsize: default is (16, 16)
        color: default is 'rebeccapurple'
    """
    df_num = df.select_dtypes(include = ['float64', 'int64'])
    pos=0
    plt.figure(figsize=figsize)
#     plt.tight_layout(w_pad=1)
    for col in df_num.columns:
        pos +=1
        plt.subplot((df_num.shape[1]/4)+1,4,pos)
        sns.boxplot(y=col, data=df_num, color=color)
    return df_num


# Plots of categorical features

def pieDF(df, figsize=(16, 16), cmap='viridis'):
    """Plots boxplots for all categorical columns in DataFrame with up to 30 values.
    Params
    ======
        df: DataFrame
        figsize: default is (16, 16)
        cmap: default is 'viridis'
    """
    df_cat = df.select_dtypes(include = 'category')
    position=0
    catWithManyValues = []
    plt.figure(figsize=figsize)
#     plt.tight_layout(w_pad=1)
    for col in df_cat.columns:
        if df[col].nunique() <= 30:
            position +=1
            plt.subplot(round(df_cat.shape[1]/4)+1,4,position)
            df[col].value_counts().plot(kind='pie', cmap = cmap)
        else: catWithManyValues.append(df[col].name)
    display("Not plotted: " + str(catWithManyValues))
    return df_cat


# Plots of CORRELATIONS
    
def corrHeatMap_num(df, figsize=(16, 16), cmap='magma'):
    """Creates heatmap to show correlations between all numerical columns in DataFrame.
    Params
    ======
        df: DataFrame
        figsize: default is (16, 16)
        cmap: default is 'magma'
    """
    plt.figure(figsize=figsize)
    df_num = df.select_dtypes(include = ['int64', 'float64'])
    sns.heatmap(df_num.corr(), cmap=cmap, linecolor='white', linewidth=1, annot=True)
    return df_num


def corrBoxDF_numClass(df, target, figsize=(16, 16), color='rebeccapurple'):
    """Creates series of boxplots to show correlation between all numerical columns and target classes value in DataFrame.
    Params
    ======
        df: DataFrame
        target: Target Variable
        figsize: default is (16, 16)
        color: default is 'rebeccapurple'
    """
    df_num = df.select_dtypes(include = ['float64', 'int64'])
    position=0
    plt.figure(figsize=figsize)
#     plt.tight_layout(w_pad=1)
    for col in df_num.columns:
        position +=1
        plt.subplot((df_num.shape[1]/2)+1,2,position)
        sns.boxplot(x=df[target].astype('category'), y=col, data=df_num, color=color)
    return df_num


def corrLineDF_numClass(df, target, figsize=(16, 16), ylim=[0,1], color='rebeccapurple'):
    """Creates series of lineplots to show correlation details between all numerical columns and target classes in DataFrame.
    Params
    ======
        df: DataFrame
        target: Target Variable (has to be in numerical format)
        figsize: default is (16, 16)
        ylim: scale of y-axis, default is [0,1]
        color: default is 'rebeccapurple'
    """
    df_num = df.select_dtypes(include = ['float64', 'int64'])
    position=0
    plt.figure(figsize=figsize)
#     plt.tight_layout(w_pad=1)
    for col in tqdm(df_num.columns):
        # df_plot = df[[col, target]].groupby(col, as_index=False).mean().sort_values(by=target, ascending=False)
        position +=1
        plt.subplot(round(df_num.shape[1]/2)+1,2,position)
        plt.ylim(ylim)
        plt.xlabel(df[col].name)
        sns.lineplot(x=col, y=target, data=df_num, color=color)
    return df_num


def corrPointDF_catClass(df, target, figsize=(16, 16), ylim=[0,1], color='rebeccapurple', cmap='viridis'):
    """Creates series of pointplots (and corresponding piecharts) to show correlations between all categorical columns 
    and target classes in DataFrame.
    Params
    ======
        df: DataFrame
        target: Target Variable (has to be in numerical format)
        figsize: default is (16, 16)
        ylim: scale of y-axis, default is [0,1]
        color: default is 'rebeccapurple'
        cmap: default is 'viridis'
    """
    df_cat = df.select_dtypes(include = ['category'])
    position=0
    plt.figure(figsize=figsize)
#     plt.tight_layout(w_pad=1)
    for col in df_cat.columns:
        df_plot = df[[col, target]].groupby(col, as_index=False).mean().sort_values(by=target, ascending=False)
        position +=1
        plt.subplot(df_cat.shape[1],2,position)
        plt.ylim(ylim)
        sns.pointplot(x=col, y=target, data=df_plot,color=color)
        if df[col].nunique() <= 30:
            position +=1
            plt.subplot(df_cat.shape[1],2,position)
            df[col].value_counts().plot(kind='pie', cmap = cmap)
        else: position +=1
    return df_cat


# corr PairPlot numCols to numTarget - see here: https://www.kaggle.com/ekami66/detailed-exploratory-data-analysis-with-python
# for i in range(0, len(df_num.columns), 5):
#     sns.pairplot(data=df_num,
#                 x_vars=df_num.columns[i:i+5],
#                 y_vars=['SalePrice'])