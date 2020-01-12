import pandas as pd
import numpy as np

# Calculates Outliers for an array
def iqr_outlier(array):
    per_75= np.nanpercentile(array,75)
    per_25= np.nanpercentile(array,25)
    IQR= per_75-per_25
    print(IQR)
    uprband= per_75+(1.5 *IQR)
    lwrband= per_25-(1.5*IQR)
    return [i for i in array if i>uprband or i<lwrband]
  #  print(i)

#Basic Data Exploration
def basic_function(df):
    print("ROWS: {} COLUMNS: {}".format(str(df.shape[0]),str(df.shape[1])))
    print('='*100)
    print(df.info())
    print('='*100)
    print("Descriptive Statistics for numerical columns:")
    print(df.describe())
    print('='*100)
    print("Descriptive Statistics for all columns:")
    print(df.describe(include='object'))
    print('='*100)
    print("Non Null Columns and Counts:")
    null_df=pd.DataFrame(df.isnull().sum())
    null_df.columns=['Count']
    print(null_df[null_df['Count'] > 0])
    print('='*100)
    df_numeric=df.select_dtypes(exclude='object')
    df_num_cols=df_numeric.columns
    for c in df_num_cols:
        print(c)
        print(iqr_outlier(df[c]))
        print('-'*100)

if __name__ == "__main__":
    df=pd.read_csv('titanic.csv')
    basic_function(df)