#streamlit run streamlit_app.py
#C:\Users\MyPC\Desktop\coding\streamlit\streamlit_app.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st

#st.header('ST.Button Example')
#st.title("ST.Button Example", text_alignment="center")
#if st.button('Say Hello'):
#    st.write('Hello There')
#else:
#    st.write('Good Bye')

st.header('st.header Example')
st.write('st.text Example')
st.header('display numbers:')
st.write(1234)
st.header('display dataframe:')
df = pd.read_excel("C:\\Users\\MyPC\\Desktop\\coding\\pandas\\mar_camp.xlsx")
st.write(df.head(5))
st.write('blow is a dataframe:' , df , 'above is a dataframe:')
st.plotly_chart(px.scatter(df, x='Spend' , y='Conversions' , color='Channel'  , hover_data=['Spend'] , title='Spend vs Conversions' ,
                           range_x=[-2500, 10000] , range_y=[0, 1000] , width=800 , height=600))
st.markdown('متن تستی', text_alignment='right')