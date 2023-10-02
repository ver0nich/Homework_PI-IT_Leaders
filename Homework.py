#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
# Загрузка CSV файла
st.title('Анализ данных с Streamlit')
st.set_option('deprecation.showPyplotGlobalUse', False)

uploaded_file = st.file_uploader("Загрузите CSV файл", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write('Превью данных:')
    st.write(df.head())

    # Выбор переменных
    st.sidebar.title('Настройки')
    x_variable = st.sidebar.selectbox('Выберите первую переменную:', df.columns)
    y_variable = st.sidebar.selectbox('Выберите вторую переменную:', df.columns)

    # Построение графиков
    st.subheader('Распределение первой переменной:')
    if df[x_variable].dtype == 'object':
        # Если переменная категориальная, строим pie chart
        plt.figure(figsize=(5, 5))
        df[x_variable].value_counts().plot.pie(autopct='%1.1f%%')
        st.pyplot()
    else:
        # Если переменная числовая, строим гистограмму
        plt.figure(figsize=(8, 6))
        sns.histplot(df[x_variable], kde=True)
        st.pyplot()

    st.subheader('Распределение второй переменной:')
    if df[y_variable].dtype == 'object':
        # Если переменная категориальная, строим pie chart
        plt.figure(figsize=(5, 5))
        df[y_variable].value_counts().plot.pie(autopct='%1.1f%%')
        st.pyplot()
    else:
        # Если переменная числовая, строим гистограмму
        plt.figure(figsize=(8, 6))
        sns.histplot(df[y_variable], kde=True)
        st.pyplot()

    # Выбор проверочного алгоритма
    st.subheader('Проверка гипотез:')
    test_type = st.selectbox('Выберите проверочный алгоритм:', ['t-тест', 'p-value тест', 'Chi-Square тест'])

    if test_type == 't-тест':
        t_statistic, p_value = stats.ttest_ind(df[x_variable], df[y_variable])
        st.write(f'Результат t-теста: t-статистика = {t_statistic}, p-значение = {p_value}')
    elif test_type == 'p-value тест':
        p_value = stats.ttest_ind(df[x_variable], df[y_variable]).pvalue
        st.write(f'Результат p-value теста: p-значение = {p_value}')
    elif test_type == 'Chi-Square тест':
        contingency_table = pd.crosstab(df[x_variable], df[y_variable])
        chi2, p_value, _, _ = stats.chi2_contingency(contingency_table)
        st.write(f'Результат Chi-Square теста: Хи-квадрат = {chi2}, p-значение = {p_value}')

else:
    st.warning('Загрузите CSV файл для начала анализа данных.')


# In[ ]:




