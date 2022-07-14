
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


def cleaning_application_train(data):

    # data.drop(['SK_ID_CURR','CODE_GENDER'],axis=1,inplace=True)
    data[data['AMT_INCOME_TOTAL'] >40000000]['AMT_INCOME_TOTAL']=np.nan
    data[data['DAYS_EMPLOYED']>100000]['DAYS_EMPLOYED']=np.nan
    data[data['OWN_CAR_AGE']>50]['OWN_CAR_AGE']=np.nan
    data[data['OBS_30_CNT_SOCIAL_CIRCLE']>340]['OBS_30_CNT_SOCIAL_CIRCLE']=np.nan
    data[data['OBS_60_CNT_SOCIAL_CIRCLE']>340]['OBS_60_CNT_SOCIAL_CIRCLE']=np.nan


    return data


def cleaning_bureau(data):
    data[data['DAYS_ENDDATE_FACT']<-40000]['DAYS_ENDDATE_FACT']=np.nan
    data[data['DAYS_CREDIT_UPDATE']<-40000]['DAYS_CREDIT_UPDATE']=np.nan
    data[data['AMT_CREDIT_MAX_OVERDUE']>.8e8]['AMT_CREDIT_MAX_OVERDUE']=np.nan
    data[data['AMT_CREDIT_SUM']>5e8]['AMT_CREDIT_SUM']=np.nan
    data[data['AMT_CREDIT_SUM_DEBT']>1.5e8]['AMT_CREDIT_SUM_DEBT']=np.nan 
    data[data['AMT_CREDIT_SUM_OVERDUE']>3.5e5]['AMT_CREDIT_SUM_OVERDUE']=np.nan 
    data[data['AMT_ANNUITY']>1e8]['AMT_ANNUITY']=np.nan

    return data



def cleaning_previous_application(data):
    data['DAYS_FIRST_DRAWING'][data['DAYS_FIRST_DRAWING'] == 365243.0] = np.nan
    data['DAYS_FIRST_DUE'][data['DAYS_FIRST_DUE'] == 365243.0] = np.nan
    data['DAYS_LAST_DUE_1ST_VERSION'][data['DAYS_LAST_DUE_1ST_VERSION'] == 365243.0] = np.nan
    data['DAYS_LAST_DUE'][data['DAYS_LAST_DUE'] == 365243.0] = np.nan
    data['DAYS_TERMINATION'][data['DAYS_TERMINATION'] == 365243.0] = np.nan
    data['AMT_APPLICATION'][data['AMT_APPLICATION'] > 5e6] = np.nan

    return data


def feature_engineering_application_train(data):

    data.drop('CODE_GENDER',axis=1,inplace=True)

    data['EXT_SOURCE']=data[['EXT_SOURCE_1', 'EXT_SOURCE_2', 'EXT_SOURCE_3']].mean(axis=1)
    data.drop(['EXT_SOURCE_1', 'EXT_SOURCE_2', 'EXT_SOURCE_3'],axis=1,inplace=True)
    negative_days=['DAYS_BIRTH','DAYS_EMPLOYED','DAYS_REGISTRATION','DAYS_ID_PUBLISH','DAYS_LAST_PHONE_CHANGE']
    for i in negative_days:
        data[i]=np.abs(data[i])

    data['DAYS_BIRTH']=np.round(data['DAYS_BIRTH']/365)

    data['DAYS_EMPLOYED']=np.round(data['DAYS_EMPLOYED']/365)

    data["PAYMENT_RATE"]=data["AMT_ANNUITY"]/data["AMT_CREDIT"]

    data["INCOME_PER_PERSON"]=data["AMT_INCOME_TOTAL"]/data["AMT_CREDIT"]

    data["INCOME_PER_PERSON_RATE"]=data["AMT_INCOME_TOTAL"]/(data["CNT_FAM_MEMBERS"]+1)

    data["DAYS_WORKING_PER"]=data["DAYS_EMPLOYED"]/data["DAYS_BIRTH"]

    data["ANNUITY_DAYS_EMPLOYED_PER"]=data["DAYS_EMPLOYED"]/data["AMT_ANNUITY"]

    data["AMT_CREDIT_DAYS_EMPLOYED"]=data["DAYS_EMPLOYED"]/data["AMT_CREDIT"]

    data['GOODS_PRICE_AFFORDABLE']=data['AMT_INCOME_TOTAL']/data['AMT_GOODS_PRICE']



    return data

def feature_engineering_bureau(data):
    
    data['ANNUITY_CREDIT_RATIO'] = data['AMT_ANNUITY'] / data['AMT_CREDIT_SUM']


    return data

def feature_engineering_bureau_balance(data):
    
    data["MONTHS_BALANCE"]=np.abs(data["MONTHS_BALANCE"])
    data['STATUS']=data['STATUS'].apply(lambda x: 'Y' if x in ['5', '1', '4', '3','0', '2'] else x)

    return data

def feature_engineering_POS_CASH_balance(data):
    
    data["MONTHS_BALANCE"]=np.abs(data["MONTHS_BALANCE"])
    data['SK_DPD'] = data['SK_DPD'].apply( lambda x: 1 if x>0 else 0)

    return data

def feature_engineering_credit_card_balance(data):
    
    data["MONTHS_BALANCE"]=np.abs(data["MONTHS_BALANCE"])
    data['SK_DPD'] = data['SK_DPD'].apply( lambda x: 1 if x>0 else 0)

    return data


def feature_engineering_installments_payments(data):
    
   data['LATE_PAYMENT_FLAG'] = (data['DAYS_ENTRY_PAYMENT'] - data['DAYS_INSTALMENT']).apply(lambda x: 1 if x>0 else 0)
   data['LESS_PAYMENT_FLAG'] = (data['AMT_PAYMENT'] - data['AMT_INSTALMENT']).apply(lambda x: 1 if x>0 else 0)

   return data


def feature_engineering_previous_application(data):
    
   data["PAYMENT_RATE"]=data["AMT_ANNUITY"]/data["AMT_CREDIT"]

   return data