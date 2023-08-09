# %%

import pandas as pd

# %%

df = pd.read_csv("../data/pedido.csv")
df

# %%

## Maniera 1 - usa-se esse aqui no dia a dia - empilha comandos
df.rename(columns={"descUF": "descEstado"})

## Maneira 2           
df.rename(columns={"descUF": "descEstado"}, inplace=True)
          
# %%