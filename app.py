import streamlit as st  
import pandas as pd  
import matplotlib.pyplot as plt  
  
# Load the stock data  
stock_data = pd.read_csv('stock_data.csv')  
stock_data['Date'] = pd.to_datetime(stock_data['Date'])  
stock_data.set_index('Date', inplace=True)  
  
# Title of the app  
st.title('Stock Price Analysis')  
  
# User inputs for date and period  
start_date = st.date_input('Select Start Date', value=pd.to_datetime('2011-10-05'))  
end_date = st.date_input('Select End Date', value=pd.to_datetime('2025-05-10'))  
  
# Filter data based on user input  
filtered_data = stock_data.loc[start_date:end_date]  
  
# Plotting the profit/loss graph  
st.subheader('Profit and Loss Over Selected Time Period')  
plt.figure(figsize=(14, 7))  
plt.plot(filtered_data['Total'], label='Total Profit/Loss', color='blue')  
plt.axhline(0, color='red', linestyle='--')  # Adding a horizontal line at zero  
plt.title('Profit and Loss Over Time')  
plt.xlabel('Date')  
plt.ylabel('Total Profit/Loss')  
plt.legend()  
plt.grid()  
st.pyplot(plt)  
  
# Recommendation logic  
latest_total = filtered_data['Total'].iloc[-1]  
previous_total = filtered_data['Total'].iloc[-2] if len(filtered_data) > 1 else None  
  
if previous_total is not None:  
    if latest_total > previous_total:  
        recommendation = "The stock price has increased. Consider buying."  
    else:  
        recommendation = "The stock price has decreased. It may not be a good time to buy."  
else:  
    recommendation = "Not enough data to make a recommendation."  
  
# Display recommendation  
st.subheader('Recommendation')  
st.write(recommendation)  