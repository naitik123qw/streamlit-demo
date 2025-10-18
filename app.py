import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
st.title("AI Student Data Analyzer")
st.subheader("welcome to the Login page")
st.write("choose who are you")
person = st.selectbox("you selected",["Admin","Student"])
st.write(f"you choose that you are a {person}")
name = st.text_input("Enter your name: ")
dob = st.date_input("Enter your date of birth")
gender = st.radio("Gender",["Male","Female"])
st.write("what is your age")
age = st.slider("Age",0,100,18)
st.write(f"ok your age is {age}")
st.sidebar.subheader(f"hii {name} ")
st.sidebar.write(f"{person}")
st.sidebar.write(f"your date of birth is {dob}")
st.sidebar.write(f"your gender is {gender}")
st.sidebar.write(f"your age is {age} year old")
if st.button("SUBMIT"):
    st.form_submit_button("Submit")
if name:
    st.success(f"Welcome {name}")
st.subheader("Welcome to the admin dashboard")
file = st.file_uploader("upload your records here",type=["csv"])
if person==Student:
    if file:
    df = pd.read_csv(file)
    st.dataframe(df)
if file:
    st.success("Students analytics dashboard ")
    st.write(df.describe())
if file:
    students = df["name"]
    filtered_student = st.selectbox("Select a target student",students)
    students_data = df[df["name"]==filtered_student]
    students_choice = students_data.columns.tolist()
    x = st.selectbox("give value for comparission ",students_choice)
    y = st.selectbox("give another value of comparisssion",students_data.columns,index = 5)
    st.subheader("line chart of student")
    st.line_chart(students_data.set_index(x)[y])
    st.subheader("bar graph of student")
    st.bar_chart(students_data.set_index(x)[y])
st.subheader("Student Study hours Predictor")
data = pd.DataFrame({
    'Marks':[50,60,70,80,90],
    'Studyhours':[2,3,4,5,6]
    })
X = data[['Marks']]
Y = data['Studyhours']
model=LinearRegression()
model.fit(X,Y)
user_marks = st.number_input("Enter marks to predict study hours",min_value=0,max_value=100,value=75)
predicted_hours = model.predict([[user_marks]])
if st.button("PREDICT"):
    st.success(f"Predicted Study Hours {predicted_hours[0]:.2f} study needed to acheive your given marks goal")
    st.line_chart(data,x='Marks',y='Studyhours')
     
    





















