
from moralis import evm_api


API_KEY = 'EEkNrAb3BrFrUj0ti6mZqflZ3m2f8Vow705K7e0AiZBuBlynRXaoNPZF6jjohcPC'

w_Address = "0xee83B1f7693af5935F9bCeEcd11c0D739C138Ad9"
t_Chains = 'bsc'
param= {
    "address": w_Address,
    "chain": t_Chains
}

#evm chains get my wallet balances
result = evm_api.token.get_wallet_token_balances(
    api_key=API_KEY,
    params= param
    
)
print(len(result))


import pandas as pd
df = pd.DataFrame(result)

print(df)

#get prices of listed tokens 
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()
print(cg.ping())
names= df['name']

print(names)
for i in names:
    results = cg.get_price(ids=i, vs_currencies='usd')
    print(results)
