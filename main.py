import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the no. of days of Forecast")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

def get_data(days):
    dates = ["2023-13-9", "2023-14-9", "2023-15-9"]
    temperatures = [10, 11, 18]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures

d,t = get_data(days)
figure = px.line(x=d, y=t, labels={"x": "Dates", "y": "Temperature (C)"})
st.plotly_chart(figure)