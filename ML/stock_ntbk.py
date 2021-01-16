import pandas_datareader as web
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Embedding
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
import math
from numpy import array
import numpy

def predict():
  df3=web.DataReader('GOOGL',data_source='yahoo',start='15-1-2016',end='15-01-2021')
  df3.to_csv("Stock_dataset.csv")
  df2=web.DataReader('TSLA',data_source='yahoo',start='15-1-2016',end='15-01-2021')
  df3.to_csv("Stock_dataset1.csv")
  df4=web.DataReader('AAPL',data_source='yahoo',start='15-1-2019',end='15-01-2021')
  df4.to_csv("Stock_dataset1.csv")
  df=pd.concat([df3, df2,df4])
  df1=df.reset_index()['Close']

  scaler=MinMaxScaler(feature_range=(0,1))
  df1=scaler.fit_transform(np.array(df1).reshape(-1,1))
  training_size=int(len(df1)*0.65)
  test_size=len(df1)-training_size
  train_data,test_data=df1[0:training_size,:],df1[training_size:len(df1),:1]
 # convert an array of values into a dataset matrix
  def create_dataset(dataset, time_step=1):
    dataX, dataY = [], []
    for i in range(len(dataset)-time_step-1):
      a = dataset[i:(i+time_step), 0]   ###i=0, 0,1,2,3-----99   100 
      dataX.append(a)
      dataY.append(dataset[i + time_step, 0])
    return numpy.array(dataX), numpy.array(dataY)

  time_step = 50
  X_train, y_train = create_dataset(train_data, time_step)
  X_test, ytest = create_dataset(test_data, time_step)
  print(X_train.shape)

  X_train =X_train.reshape(X_train.shape[0],X_train.shape[1] , 1)
  X_test = X_test.reshape(X_test.shape[0],X_test.shape[1] , 1)

  print(X_train.shape)

  model=Sequential()
  model.add(LSTM(50,return_sequences=True,input_shape=(50,1)))
  model.add(LSTM(50,return_sequences=True))
  model.add(LSTM(50))
  model.add(Dense(1))
  model.compile(loss='logcosh',optimizer='adam',metrics = ['mse'])

  model.fit(X_train,y_train,validation_data=(X_test,ytest),epochs=10,batch_size=64,verbose=1)

  train_predict=model.predict(X_train)
  test_predict=model.predict(X_test)

  train_predict=scaler.inverse_transform(train_predict)
  test_predict=scaler.inverse_transform(test_predict)
  model.save('STOCKS.h5')

  look_back=50
  x_input=test_data[341:].reshape(1,-1) #previous 100 days data
  x_input.shape
  temp_input=list(x_input)
  temp_input=temp_input[0].tolist()


  lst_output=[]
  n_steps=719
  i=0
  while(i<1):
      
      if(len(temp_input)>100):
          #print(temp_input)
          x_input=np.array(temp_input[1:])
          #print("{} day input {}".format(i,x_input))
          x_input=x_input.reshape(1,-1)
          x_input = x_input.reshape((1, n_steps, 1))
          #print(x_input)
          yhat = model.predict(x_input, verbose=0)
          print("{} day output {}".format(i,yhat))
          temp_input.extend(yhat[0].tolist())
          temp_input=temp_input[1:]
          #print(temp_input)
          lst_output.extend(yhat.tolist())
          i=i+1
      else:
          x_input = x_input.reshape((1, n_steps,1)) #reshape for new data
          yhat = model.predict(x_input, verbose=0)
          #print(yhat[0])
          temp_input.extend(yhat[0].tolist())#adding yhat
          #print(len(temp_input))
          lst_output.extend(yhat.tolist())
          i=i+1
          return lst_output
      
print(predict())