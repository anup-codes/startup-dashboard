import streamlit as st
import pandas as pd
import time

#text utility..................................................................................................

st.title('Startup Dashboard')
st.header('i am learner ')
st.subheader('and love this ')
st.write('this is a normal text')

st.markdown("""
### my favorite movies 
        -Race 3
        -Housefuls
        -Housefull
""")

st.code("""
def foo(input):
        return foo**2
""")

st.latex('x^2 + y^2 + 2 = 0')

# Display Elements..................................................................................


df = pd.DataFrame({
  'name':['nitish','Shivam ','ankit'],
  'marks':[50,60,70],
  'package': [10,12,14]
})

st.dataframe(df)

st.metric('Revenue','Rs 3L','3%')

st.json({
  'name':['nitish','Shivam ','ankit'],
  'marks':[50,60,70],
  'package': [10,12,14]
})

#displaying media........................................................................
st.image('kmclu.png')
# st.video('')
#st.audio('')

# Creating Layouts..........................................................................
st.sidebar.title('sidebar')

col1, col2 = st.columns(2)

with col1 :
  st.image('kmclu.png')

with col2 :
  st.image('kmclu.png')


#showing status........................................................

st.error('Login Failed')
st.success('Login Done')
st.warning('doing wrong')
st.info('logggginnn')


bar = st.progress(0)
for i in range(1,101):
  #time.sleep(0.1)
  bar.progress(i)


#Taking User Input.............................................

email = st.text_input('enter email')
number = st.number_input('enter age')
date = st.date_input('enter dob')

btn = st.button('login')

#if btn get clicked then perform this action
if btn:
  st.success('Login Done')
  st.balloons()
  #to print on screen
  st.write(email)

#dropdown
st.selectbox('select gender',['m','f'])

#file uploder
file= st.file_uploader('upload a csv file')

if file is not None:
  df = pd.read_csv(file)
  st.dataframe(df.head(10))