
import numpy as np
import plotly.graph_objs as go
from datetime import datetime
from datetime import datetime, timedelta
from streamlit_timeline import st_timeline
import streamlit as st

def generate_example_data(year=2024):
    # gerando uma data para cada dia do ano
    numdays = 365 + (1 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 0)  # account for leap year
    base = datetime(year, 1, 1)
    date_list = [base + timedelta(days=x) for x in range(numdays)]

    # gerando um número aleatório de contribuições para cada dia
    contributions = np.random.randint(1, 5, size=numdays)

    return date_list, contributions


def heatmap(dates, contribs):
    # Mapeamento de números para nomes de mês
    month_mapping = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep',
                     10: 'Oct', 11: 'Nov', 12: 'Dec'}
    week_mapping = {0: 'Seg', 1: 'Ter', 2: 'Qua', 3: 'Qui',4:'Sex',5:'Sab',6:'Dom'}

    # Mapeamento de datas para eixos x (semana do ano) e y (dia da semana)
    week_of_year = [date.isocalendar()[1] for date in dates]
    day_of_week = [date.weekday() for date in dates]  # Monday is 0 and Sunday is 6

    # Crie um mapeamento de semana do ano para mês
    week_to_month = {week: month_mapping[dates[i].month] for i, week in enumerate(week_of_year)}

    x_labels = list(week_to_month.values())
    y_labels = [week_mapping[day] for day in day_of_week]

    label = ''
    x_label = [[x_labels[i], (label := x_labels[i])][0] if x_labels[i] != label else '' for i in range(len(x_labels))]

    layout = go.Layout(
        title='Registro de eventos ao longo do ano de 2024',
        xaxis=dict(
            title='Mês do ano',
            tickvals=list(week_to_month.keys()),  # Posições dos ticks
            ticktext=x_label  # Texto dos ticks
        ),
        yaxis=dict(
            title='Dia da semana',
            # tickvals=y_labels,
            # ticktext=list(week_mapping.values())
        ),
    )

    # Criar um calendário de contribuições usando Heatmap
    heatmap = go.Heatmap(
        x=week_of_year,
        y=day_of_week,
        z=contribs,
        type='heatmap',
        colorscale='Blues'
    )

    return go.Figure(data=[heatmap], layout=layout)

def timeline(df):
    items = [
        {"id": 1, "content": "2022-10-20", "start": "2022-10-20"},
        {"id": 2, "content": "2022-10-09", "start": "2022-10-09"},
        {"id": 3, "content": "2022-10-18", "start": "2022-10-18"},
        {"id": 4, "content": "2022-10-16", "start": "2022-10-16"},
        {"id": 5, "content": "2022-10-25", "start": "2022-10-25"},
        {"id": 6, "content": "2022-10-27", "start": "2022-10-27"},
    ]

    print(df)
    df['start'] = df['start'].apply(lambda x: x.strftime('%Y-%m-%d %H:%M:%S'))
    items = [df.iloc[i].to_dict() for i in range(len(df))]
    print(items)

    timeline = st_timeline(items, groups=[], options={}, height="300px")
    st.subheader("Selected item")
    st.write(timeline)