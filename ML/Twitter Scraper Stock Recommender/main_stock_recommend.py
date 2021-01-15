#Importing Packages

import pandas_datareader as web
import numpy as np
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import tweepy as tw
import numpy as np
import pandas as pd
import pandas_datareader as web
import math
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import datetime as dt
import plotly
import constants as ct
from textblob import TextBlob

from Tweet import Tweet
#Importing Scripts:

from get_stock_data import get_stock_data
from stock_forecasting import stock_forecasting
from retrieving_tweets_polarity import retrieving_tweets_polarity
from recommending_with_d import recommending_with_d

num_of_tweets=20


consumer_key="SvrmVjZ527gKMocaCIdS8ArZo"
consumer_secret="mFjrSeMr6TU7qOxQHTrtyPGt2BeA4RnBK4XzIHo1SH4jGebyl2"
access_token="2555973745-UzdXECQl5iom7CLhLVvsSEPZLdPC6kWsVHR3O4o"
access_token_secret="8sJRoJgPTxkqNt5fFe37nOq8fsMSVNABqv9VyTuYCqnrI"



def get_stock_recommend(symbol,from_date,to_date):
    df=get_stock_data(symbol, from_date, to_date)
    df, forecast_out=stock_forecasting(df)
    global_polarity=retrieving_tweets_polarity(symbol)
    res=recommending_with_d(df, forecast_out, global_polarity)
    return res
    