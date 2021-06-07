import pandas as pd
d=pd.read_csv("penerbitan_akta_kelahiran_Banda_aceh_2016_2020.csv")
print (d)
d.info()
import numpy as np
import matplotlib.pyplot as plt
d['prediksi']=d.iloc[:,0].rolling(window=3).mean()
print(d)
d['prediksi']=d['prediksi'].replace(np.nan,0)
print(d)
from sklearn.metrics import mean_squared_error
mse=mean_squared_error(d['prediksi'],d['Akte_Kelahiran'])
rmse=np.sqrt(mse)
print("MSE: ",mse)
print("RMSE: ",rmse)
a=range(len(d))
plt.scatter(a, d['Akte_Kelahiran'], color='green')
plt.plot(a, d['prediksi'], color='red')
plt.title('Hasil Prediksi Penerbitan Akte Kelahiran di Banda Aceh')
plt.xlabel('Data ke-')
plt.ylabel('Akte_Kelahiran')
plt.show()