import numpy as np
import pandas as pd

def funCleanNumericals(df):
    df['SUM_INVOICE_AMOUNT'].replace(0.0, np.NaN, inplace=True)
    # replacing ownerAge where implausible with Altersklasse 1J, setting age 0 to NaN
    df['ownerAge'] = np.where((df['ownerAge'] >= 90) | (df['ownerAge'] < 18) | (df['ownerAge'].isnull()), 
                              df['Altersklasse1J'], df['ownerAge'])
    df['ownerAge'].replace(0.0, np.NaN, inplace=True)
    df = df[df['age_mnth'] <= 96]
    return df

def funCleanStrings(df):
    df['SALES_TYPE'] = df['SALES_TYPE'].str.split(' ').str.get(0)
    df['SALES_TYPE'] = df['SALES_TYPE'].astype('category')
    return df

def funCleanMissingStates(df):
    # set missing partner states to "FL"
    df['PARTNER_STATE'] = np.where((df['PARTNER_STATE'].isnull()),"FL", df['PARTNER_STATE'])
    # set missing customer state = partner state where distance to partner < 20 km
    df['PERSON_STATE'] = np.where((df['PERSON_STATE'].isnull()) & (df['dist_metres_log'] <= np.log10(20000)),
                                                                      df['PARTNER_STATE'], df['PERSON_STATE'])
    df[['PARTNER_STATE', 'PERSON_STATE']] = df[['PARTNER_STATE', 'PERSON_STATE']].astype('category')
    return df

def funCleanCategoricals(df):
    df['target_event'] = df['target_event'].map({'ACTIVE':0, 'CHURN':1}).astype(np.int64)
    df = df[df['ACTIVE'] == 1]
    return df