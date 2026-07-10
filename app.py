import streamlit as st
import pandas as pd

df= pd.read_csv('F:\Pythonn\startup-dashboard\startup_cleaned.csv')
#data cleaning...............
# df['Investors Name']=df['Investors Name'].fillna('Undisclosed')

def load_investor_details(investor):
 
  st.title(investor)

  #load the recent 5 investment of the investor
  last5_df = df[df['investors'].str.contains(investor)].head()[['date','startup','vertical','city','round','amount']]
  st.subheader('Most Recent Investments')
  st.dataframe(last5_df)


  #biggest investments
  big_df = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending = False).head()
  st.subheader('Biggest Investments')
  st.dataframe(big_df)




st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('Select One', ['Overall Analysis','StartUp', 'Investor'])


if option == 'Overall Analysis':
  st.title('Overall Analysis')
elif option == 'StartUp':
  st.sidebar.selectbox('Select startup',sorted(df['startup'].unique()))
  btn1 = st.sidebar.button('Find Startup Details')
  st.title('StartUp Analysis')

else:
  selected_investor = st.sidebar.selectbox('Select startup',sorted(set(df['investors'].str.split(',').sum())))
  btn2 = st.sidebar.button('Find Investor Details')
  
  if btn2:
    load_investor_details(selected_investor)
  


