# %% 

import pandas as pd

# %% 

df = pd.read_csv("../data/pedido.csv")

 # %% 

idade = pd.Series([20, 14, 13, 67, 54, 19, 24])

idade[idade >=20]

# %%


df.head()
# %%
