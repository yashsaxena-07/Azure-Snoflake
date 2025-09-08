import pandas as pd

df=pd.read_csv("./Azure/Day 1/Lab2/sales_data.csv")

print(df.head())



print(df.head())


#df.dropna(inplace=True)  # Remove rows with missing values
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df.dropna(subset=["quantity", "price"], inplace=True) 

# print(df.head())

df.drop('Unnamed: 6',axis=1,inplace=True)

print(df.head())
print()

df["quantity"] = df["quantity"].astype(int)
df["price"] = df["price"].astype(int)

df['revenue']=df['price']*df['quantity']

product_revenue = df.groupby("product")["revenue"].sum().reset_index()
print(product_revenue.head())
print()
product_revenue.to_csv("/Users/yashsaxena7007/Desktop/External Trainer/Azure+Snowflake/Azure/Lab2/product_revenue.csv", index=False)


top_cust=df.groupby('customer_id')["revenue"].sum().reset_index()
top_cust.rename(columns={"revenue": "total_spending"}, inplace=True)
top_cust = top_cust.sort_values(by="total_spending", ascending=False).head(5)
print(top_cust.head())
print()
top_cust.to_csv("/Users/yashsaxena7007/Desktop/External Trainer/Azure+Snowflake/Azure/Lab2/top_customers.csv", index=False)

df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
df.dropna(subset=["order_date"], inplace=True)
df["month"] = df["order_date"].dt.to_period("M").astype(str)
monthly_orders = df.groupby("month")["order_id"].count().reset_index()
monthly_orders.rename(columns={"order_id": "total_orders"}, inplace=True)
print(monthly_orders.head())
print()
monthly_orders.to_csv("/Users/yashsaxena7007/Desktop/External Trainer/Azure+Snowflake/Azure/Lab2/monthly_orders.csv", index=False)