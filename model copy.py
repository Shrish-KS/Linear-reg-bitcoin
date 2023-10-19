import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

path_to_dataset = 'bitstampUSD_1-min_data_2012-01-01_to_2021-03-31.csv'
bitcoin_dataset = pd.read_csv(path_to_dataset)
bitcoin_dataset.isnull().sum()
bitcoin_dataset.dropna(inplace=True)
bitcoin_dataset.info()
bitcoin_dataset=bitcoin_dataset.drop(bitcoin_dataset.columns[0],axis=1)
y=np.array(bitcoin_dataset["Close"])
bitcoin_dataset=bitcoin_dataset.drop(bitcoin_dataset.columns[3],axis=1)

def mean_square_error(dataset,y,w,b):
    result=(np.dot(dataset,w)-y+b)*(np.dot(dataset,w)-y+b)
    result=sum(result)
    result/=(2*len(y))
    return result

def error(dataset,y,w,b):
    result=(np.dot(dataset,w)-y+b)
    print()
    return result

def cal(dataset,y,iter,alpha):
    w=[0,0,0,0,0,0]
    b=0
    m=len(y)
    for i in range(iter):
        print(np.dot(w,dataset.iloc[0]),"f")
        errors=error(dataset,y,w,b)
        w=w-((alpha/m)*(np.dot(errors,dataset)))
        print(w,b)
        print()
        print(mean_square_error(dataset,y,w,b))
        b=b-((alpha/m)*(sum(errors)))
    return [w,b]

print(bitcoin_dataset.iloc[0])
print("fr")

print(cal(bitcoin_dataset,y,20000,0.00000000005))
#[0.2447363995233102, 0.24488556893616667, 0.2445931091593409, -4.3324159944773504e-05, 0.000622325098390896, 0.24473759071936477]
#[0.25000000955460827, 0.2501536210163762, 0.2498548510514116, -4.434202534655644e-05, 5.089895014115215e-07, 0.25000251419919683]