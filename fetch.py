import yfinance as yf
import pandas as pd
from config import TICKER_CL, TICKER_OVX, START

def fetch_data(start = START) -> pd.DataFrame:
    cl_data = yf.download(TICKER_CL, start=start)[['Close', 'Volume']].rename(columns = {'Close': 'cl_close', 'Volume': 'cl_volume'})
    ovx_data = yf.download(TICKER_OVX, start=start)[['Close']].rename(columns = {'Close': 'ovx_close'})
    df = pd.concat([cl_data, ovx_data], axis = 1).dropna()
    return df