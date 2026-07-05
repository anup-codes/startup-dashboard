import streamlit as st
import pandas as pd

df= pd.read_csv('startup_funding.csv')
#data cleaning...............
df['Investors Name']=df['Investors Name'].fillna('Undisclosed')

st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('Select One', ['Overall Analysis','StartUp', 'Investor'])


if option == 'Overall Analysis':
  st.title('Overall Analysis')
elif option == 'StartUp':
  st.sidebar.selectbox('Select startup',sorted(df['Startup Name'].unique()))
  btn1 = st.sidebar.button('Find Startup Details')
  st.title('StartUp Analysis')

else:
  st.sidebar.selectbox('Select startup',sorted(df['Investors Name'].unique()))
  btn2 = st.sidebar.button('Find Investor Details')
  st.title('Investor Analysis')