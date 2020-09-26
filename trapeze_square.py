
import streamlit as st





st.write("""
# Trapeze square web app\n
Author: **Damian Nowak**
""")


st.sidebar.header('User Input Features')

aa = float(3.77788)
st.header('Square area.')
aa = st.sidebar.text_area("Lenght of the square side.", aa)
aa1 = float(aa)
base = aa1*aa1
base



bb = float(34)
bb1 = float(12)
st.header('Rectangle area.')
bb = st.sidebar.text_area("1st Lenght of the rectangle side.", bb)
bb1 = st.sidebar.text_area("2nd Lenght of the rectangle side.", bb1)

bb11 = float(bb)
bb111 = float(bb1)
base1 = bb11*bb111
base1


data1 = float(4.67)
data2 = float(23.45)
data3 = float(22.87)

st.header('Trapeze area.')


a = st.sidebar.text_area("The first base of the trapeze.", data1)
b = st.sidebar.text_area("The second base of the trapeze.", data2)
h = st.sidebar.text_area("The height of the trapeze.", data3)

a1 = float(a)
b1 = float(b)
h1 = float(h)

baseData = 0.5*(a1+b1)*h1
baseData


abc = float(87.7654)
st.header('Volume of the cube.')
abc1 = st.sidebar.text_area("The edge of the cube.", abc)

abc1 = float(abc)
base2 = abc*abc*abc
base2