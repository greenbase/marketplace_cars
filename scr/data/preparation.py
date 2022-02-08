# %%
import sys
sys.path.append("/home/daniel/marketplace_cars/scr/")
import pandas as pd
import numpy as np
from datetime import datetime
import config
#%%
# load data
path=config.ROOT/"data/raw/Marktplatz_Autos_2021.csv"
marketplace_cars=pd.read_csv(path,header=0,index_col=False,delimiter=";",decimal=",",dtype={"value":np.int16})

marketplace_cars.drop(["area","sensor"],axis=1,inplace=True)

marketplace_cars["timestamp"]=pd.to_datetime(marketplace_cars["timestamp"],format="%d.%m.%Y %H:%M:%S")

marketplace_cars
# %%
marketplace_cars.to_csv("/home/daniel/marketplace_cars/data/interim/Marktplatz_Autos_2021.csv")
# %%