import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
orders = pd.read_csv('olist_orders_dataset.csv')
payments = pd.read_csv('olist_order_payments_dataset.csv')
order_items = pd.read_csv('olist_order_items_dataset.csv')
products = pd.read_csv('olist_products_dataset.csv')

# Merge order_items and products for product categories
order_items = order_items.merge(products[['product_id', 'product_category_name']], on='product_id', how='left')

# Sidebar
st.sidebar.title("Filters")
selected_status = st.sidebar.multiselect(
    "Select Order Status",
    options=orders['order_status'].unique(),
    default=orders['order_status'].unique()
)

selected_payment = st.sidebar.multiselect(
    "Select Payment Method",
    options=payments['payment_type'].unique(),
    default=payments['payment_type'].unique()
)

# Filter data
filtered_orders = orders[orders['order_status'].isin(selected_status)]
filtered_payments = payments[payments['payment_type'].isin(selected_payment)]

# Main Page
st.title("Brazilian E-commerce Final Dashboard")
st.markdown("## Summary Insights")

# Order Status Distribution
st.subheader("Order Status Distribution")
fig, ax = plt.subplots()
sns.countplot(x='order_status', data=filtered_orders, order=filtered_orders['order_status'].value_counts().index, palette='viridis')
plt.xticks(rotation=45)
st.pyplot(fig)

# Payment Method Distribution
st.subheader("Payment Method Distribution")
fig, ax = plt.subplots()
sns.countplot(x='payment_type', data=filtered_payments, order=filtered_payments['payment_type'].value_counts().index, palette='Set2')
plt.xticks(rotation=45)
st.pyplot(fig)

# Top 10 Product Categories
st.subheader("Top 10 Product Categories")
top_categories = order_items['product_category_name'].value_counts().nlargest(10)
fig, ax = plt.subplots()
sns.barplot(y=top_categories.index, x=top_categories.values, palette='coolwarm')
st.pyplot(fig)

st.markdown("### This dashboard provides interactive filters to explore Brazilian E-commerce data!")