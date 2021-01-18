import tensorflow as tf
import pandas_datareader as web
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt


def getstock(name):
    return web.DataReader(
        name, data_source="yahoo", start="15-1-2020", end="15-01-2021"
    )


def buyorsell(df):
    M = tf.keras.models.load_model("./ML/Models/STOCKS.h5")

    df_close = df["Close"]
    scaler = MinMaxScaler(feature_range=(0, 1))
    df_close_scaled = scaler.fit_transform(np.array(df_close).reshape(-1, 1))
    print("Length of data is ",len(df_close_scaled))

    if not PROD:
        df_close_scaled = df_close_scaled[-500:]

    pred = []
    for i in range(len(df_close_scaled) - 50):
        inp = df_close_scaled[i : i + 50]
        pred.append((i + 50, np.squeeze(inp[-1] > M.predict(inp.reshape(1, 50, 1)))))

    # will refactor this later
    result = []
    z = [None, None]
    for i in pred:
        if z[0] == None and i[1] == True:
            z[0] = i[0]

        if z[0] != None and i[1] == False:
            z[1] = i[0]
            result.append(z)
            z = [None, None]

    if not PROD:
        for i in result:
            c = "r" if df_close_scaled[i[0]] > df_close_scaled[i[1]] else "g"
            plt.axvspan(i[0], i[1], color=c, alpha=0.5)

        print(result)
        print(pred)
        plt.plot(df_close_scaled)
        plt.show()


    buy = []
    sell = []
    response_data = []
    for i,j in enumerate(df_close.values):
        response_data.append({"x": i,"y":j})
        for ii in result:
            if i == ii[0]:
                buy.append({"x": i,"y":j})
            if i == ii[1]:
                sell.append({"x": i,"y":j})

    return {"res_data":response_data,"buy":buy,"sell":sell}


PROD = True

if __name__ == "__main__":
    print("works")
    stock_name = "TSLA"
    df = getstock(stock_name)
    print(buyorsell(df))
