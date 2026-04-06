import streamlit as st
import requests

st.title("Сервис кредитного скоринга")

with st.form("Подать заявку"):
    age = st.number_input("Ваш возраст", min_value=0)
    income = st.number_input("Ваш доход (тыс.руб)", min_value=0)
    education = st.checkbox("Есть ли высшее образование?")
    work = st.checkbox("Есть ли постоянная работа?")
    car = st.checkbox("Есть ли личный автомобиль?")
    submit = st.form_submit_button("Подать заявку")

if submit:
    data = {"age": age, "income": income, "education": education, "work": work, "car": car}
    response = requests.post("http://127.0.0.1:8000/score", json=data)
    st.write(response.json())
    if response.json()["approved"]:
        st.success("Поздравляем, ваша заявка одобрена")
    else:
        st.success("Ваша заявка отклонена, не расстраивайтесь!")