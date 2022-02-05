# %%
import pandas as pd
import numpy as np
from datetime import datetime
#%%
# load data
path="/home/daniel/marketplace_cars/data/raw/Marktplatz_Autos_2021.csv"
marketplace_cars=pd.read_csv(path,header=0,index_col=False,delimiter=";",decimal=",",dtype={"value":np.int16})

marketplace_cars.drop(["area","sensor"],axis=1,inplace=True)

marketplace_cars["timestamp"]=pd.to_datetime(marketplace_cars["timestamp"],format="%d.%m.%Y %H:%M:%S")

marketplace_cars
# %%
