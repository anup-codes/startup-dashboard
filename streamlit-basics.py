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
  time.sleep(0.1)
  bar.progress(i)


#Taking User Input.............................................

