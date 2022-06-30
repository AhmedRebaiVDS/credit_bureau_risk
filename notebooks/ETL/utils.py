
import numpy as np
import dask.dataframe as dd 

def reduce_mem_usage(df, verbose=True):
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    start_mem = df.memory_usage().sum() / 1024**2    
    for col in df.columns:
        col_type = df[col].dtypes
        if col_type in numerics:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == 'int':
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                       df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)  
            else:
                if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                    df[col] = df[col].astype(np.float16)
                elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)    
    end_mem = df.memory_usage().sum() / 1024**2
    if verbose: print('Mem. usage decreased to {:5.2f} Mb ({:.1f}% reduction)'.format(end_mem, 100 * (start_mem - end_mem) / start_mem))
    return df


def cleaning(data):
    data=reduce_mem_usage(data)
    data.drop(['SK_ID_CURR','CODE_GENDER'],axis=1,inplace=True)
    # data.drop(['AMT_GOODS_PRICE','ELEVATORS_MODE', 'APARTMENTS_MODE', 'TOTALAREA_MODE','BASEMENTAREA_MEDI','ENTRANCES_MEDI','LIVINGAREA_MEDI','APARTMENTS_MEDI','ELEVATORS_MODE','NONLIVINGAPARTMENTS_MODE','APARTMENTS_AVG','LIVINGAPARTMENTS_MEDI','COMMONAREA_MEDI','LIVINGAREA_AVG','LIVINGAPARTMENTS_AVG','ELEVATORS_AVG'],axis=1,inplace=True)
    data[data['AMT_INCOME_TOTAL'] >40000000]['AMT_INCOME_TOTAL']=np.nan
    data[data['DAYS_EMPLOYED']>100000]['DAYS_EMPLOYED']=np.nan
    data[data['OWN_CAR_AGE']>50]['OWN_CAR_AGE']=np.nan
    data['EXT_SOURCE']=data[['EXT_SOURCE_1', 'EXT_SOURCE_2', 'EXT_SOURCE_3']].mean(axis=1)
    data.drop(['EXT_SOURCE_1', 'EXT_SOURCE_2', 'EXT_SOURCE_3'],axis=1,inplace=True)
    categorical=data.select_dtypes('object').columns
    numeric=list(data.select_dtypes('float64').columns.values) +list(data.select_dtypes('float16').columns.values) + list(data.select_dtypes('int32').columns.values)+ list(data.select_dtypes('int16').columns.values)+ list(data.select_dtypes('int8').columns.values)+list(data.select_dtypes('float32').columns.values)
    for i in categorical:
        data[i]=data[i].fillna(data[i].mode()[0]) 
    for i in numeric:
        if(data[i].mean()==np.nan):
            data[i]=data[i].fillna(data[i].mean())
        else : 
            data[i]=data[i].fillna(0)
    
    # data=dd.get_dummies(data,drop_first=True)


    negative_days=['DAYS_BIRTH','DAYS_EMPLOYED','DAYS_REGISTRATION','DAYS_ID_PUBLISH','DAYS_LAST_PHONE_CHANGE']

    for i in negative_days:
        data[i]=np.abs(data[i])

    data['DAYS_BIRTH']=np.round(data['DAYS_BIRTH']/365)
    data['DAYS_EMPLOYED']=np.round(data['DAYS_EMPLOYED']/365)

    return data



