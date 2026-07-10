import streamlit as st
import pandas as pd

df= pd.read_csv('F:\Pythonn\startup-dashboard\startup_cleaned.csv')
#data cleaning...............
# df['Investors Name']=df['Investors Name'].fillna('Undisclosed')

st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('Select One', ['Overall Analysis','StartUp', 'Investor'])


if option == 'Overall Analysis':
  st.title('Overall Analysis')
elif option == 'StartUp':
  st.sidebar.selectbox('Select startup',sorted(df['startup'].unique()))
  btn1 = st.sidebar.button('Find Startup Details')
  st.title('StartUp Analysis')

else:
  st.sidebar.selectbox('Select startup',sorted(set(df['investors'].str.split(',').sum())))
  btn2 = st.sidebar.button('Find Investor Details')
  st.title('Investor Analysis')


