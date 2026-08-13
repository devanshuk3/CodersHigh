import pandas as pd

df = pd.read_csv("data.csv")
df["Close"] = pd.to_numeric(df["Close"])

min_price = float("inf")
max_profit = 0  

buy_day = ""
sell_day = ""
current_buy_day = ""

for i in range(len(df)):
    price = df.loc[i, "Close"]

    #find the lowest price seen so far
    if price<min_price:
        min_price = price
        current_buy_day = i

    #calculate profit if we sell today (Greedyyy approach) 
    profit = price - min_price

    #check if this is the biggest profit
    if profit>max_profit:
        max_profit=profit
        buy_day=current_buy_day
        sell_day=i

print("Buy date:", df.loc[buy_day, "Date"], df.loc[buy_day, "Close"])
print("selling date:", df.loc[sell_day, "Date"], df.loc[sell_day, "Close"])
print("Maximum profit:", max_profit)