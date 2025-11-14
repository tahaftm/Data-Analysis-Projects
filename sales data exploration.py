import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
data = pd.read_csv("C:\\Users\\USER\\Desktop\\microsoft\\module 2\\projects\Amazon Sale Report.csv", parse_dates=['Date'])
# # Time Series: Analyze sales trends over months/years.
# group = data.groupby(data["Date"].dt.strftime('%B'))['index'].count().reset_index().rename(columns={'Date' : 'Month', 'index' : 'Orders'})
# plt.plot(group['Month'], group['Orders'])
# plt.title('Monthly Orders Report')
# plt.xlabel('Months')
# plt.ylabel('Orders')
# plt.show()

# # Geographic: Determine the top-performing regions/cities.
# data['ship-city'] = data['ship-city'].str.lower()
# geograph = data.groupby('ship-city')['index'].size().reset_index(name = 'index').sort_values(by='index', ascending = False)
# max_sales = geograph.head(5)
# plt.bar(max_sales['ship-city'], max_sales['index'])
# plt.title('Distribution of Ship Cities')
# plt.show()

# # Customer Behavior: Identify the best customers or most profitable product categories.
# categories = data.groupby('Category')['index'].size().reset_index(name = 'index').sort_values(by = 'index', ascending=False)
# top_5 = categories.head(5)
# plt.bar(top_5['Category'],top_5['index'])
# plt.title('Distribution of Order Amounts')
# plt.xlabel('Order Amount')
# plt.ylabel('Frequency')
# plt.show()
