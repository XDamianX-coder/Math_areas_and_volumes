
import streamlit as st



##########################################
##########################################

st.write("""
# Fields of surface of figures \n
# and volume of solids web app\n
Author: **Damian Nowak**\n
Remember that only you can choose unit of the area,\n
so input your data only in the same units.\n
If you are calculating the area value in square meters,\n
use meters in input data and so on with other units such\n
like centimetres, millimetres, decimetres or micrometers.\n
""")

##########################################
##########################################

st.sidebar.header('User Input Features')

aa = float(3.77788)
st.header('Square area')
st.latex("Equation: Area = (length\ of\ the\ square\ side) ^ 2")
aa = st.sidebar.text_area("The length of the square side.", aa)
aa1 = float(aa)
base = aa1*aa1
base

##########################################
##########################################

bb = float(34)
bb1 = float(12)
st.header('Rectangle area')
st.latex("Equation: Area = 1st\ base\ length\ *\ 2nd\ base\ length")
bb = st.sidebar.text_area("1st Length of the rectangle side.", bb)
bb1 = st.sidebar.text_area("2nd Length of the rectangle side.", bb1)

bb11 = float(bb)
bb111 = float(bb1)
base1 = bb11*bb111
base1


##########################################
##########################################

data1 = float(4.67)
data2 = float(23.45)
data3 = float(22.87)

st.header('Trapeze area')
st.latex("Equation: Area = ((first\ base\ length\ + second\ base length)\ *\ height) /2")


a = st.sidebar.text_area("The first base of the trapeze.", data1)
b = st.sidebar.text_area("The second base of the trapeze.", data2)
h = st.sidebar.text_area("The height of the trapeze.", data3)

a1 = float(a)
b1 = float(b)
h1 = float(h)

baseData = 0.5*(a1+b1)*h1
baseData

##########################################
##########################################

st.header('Parallelogram area')
st.latex("Equation: Area = base\ length\ *\ height")
dc = float(23.56)
dc1 = float(123.654)
dd = st.sidebar.text_area("The base lenght of the parallelogram.", dc)
dd1 = st.sidebar.text_area("The height of the parallelogram.", dc1)
ddd = float(dd)
ddd1 = float(dd1)
baseData5 = ddd*ddd1
baseData5

##########################################
##########################################

st.header('Cirlce area')
st.latex("Equation: Area = π\ *\ (radius\ of\ the\ circle) ^ 2")
pi1 = float(22)
pi2 = float(7)
pi3 = float(pi1/pi2)
rr = float(23.65412)
rr1 = st.sidebar.text_area("The radius of the circle.", rr)
rr11 = float(rr1)
basecircle = pi3*rr11*rr11
basecircle

##########################################
##########################################

abc = float(87.7654)
st.header('Volume of the cube')
st.latex("Equation: Area = (the\ length\ of\ edge) ^ 3")
abc1 = st.sidebar.text_area("The length of edge of the cube.", abc)

abc1 = float(abc)
base2 = abc*abc*abc
base2

##########################################
##########################################
a11 = float(87.7654)
b11 = float(32.765)
c11 = float(234.765)
st.header('Volume of the cuboid')
st.latex("Equation: Area = 1st\ edge\ length\ *\ 2nd\ edge\ length\ *\ 3rd\ edge\ length")
a111 = st.sidebar.text_area("The 1st edge length of the cuboid.", a11)
b111 = st.sidebar.text_area("The 2nd edge length of the cuboid.", a11)
c111 = st.sidebar.text_area("The 3rd edge length of the cuboid.", a11)


a111 = float(a111)
b111 = float(b111)
c111 = float(c111)

base33 = a111*b111*c111
base33
##########################################
##########################################

Ra1 = float(123.321)
st.header('Volume of the sphere')
Ra1 = st.sidebar.text_area("The radius the sphere.", Ra1)
st.latex("Equation: Area = 4/3 *\ π\ *\ radius\ of\ the\ sphere")
Ra11 = float(Ra1)
base22 = 4/3*pi3*Ra11*Ra11*Ra11
base22

##########################################
##########################################

Ra2 = float(123.321)
hig = float(21312.78)
st.header('Volume of the cone')

st.latex("Equation: Area = (π\ *\ radius^2\ *\ height)/3 ")
Ra2 = st.sidebar.text_area("The radius of the cone.", Ra1)
hig = st.sidebar.text_area("The height of the cone.", hig)


Ra22 = float(Ra2)
hig1 = float(hig)
base223 = (pi3*Ra22*Ra22*hig1)/3
base223



##########################################
##########################################
