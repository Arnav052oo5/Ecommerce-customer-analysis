import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("purchases.csv")

# Create total purchase column
df["total_purchase"] = df["quantity"] * df["price"]

# Display dataset
print(df)

# Total spending per customer
customer_spending = df.groupby("customer_name")["total_purchase"].sum()
print("\nCustomer Spending:\n", customer_spending)

# Top customer
top_customer = customer_spending.idxmax()
print("\nTop Customer:", top_customer)

# Product popularity
product_sales = df.groupby("product")["quantity"].sum()
print("\nProduct Popularity:\n", product_sales)

# City-wise revenue
city_revenue = df.groupby("city")["total_purchase"].sum()
print("\nCity Revenue:\n", city_revenue)

# Optional chart
product_sales.plot(kind='bar', title='Product Sales')
plt.show()