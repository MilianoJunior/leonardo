
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
    '''Exibir uma linha do tempo de atividades.'''

    # Primeiro, certifique-se de que a coluna 'start' esteja no formato correto de data
    df['start'] = df['start'].apply(lambda x: x.strftime('%Y-%m-%d %H:%M:%S'))

   # Crie um novo dataframe que conta as ocorrências de cada data
    items = [df.iloc[i].to_dict() for i in range(len(df))]

    # Formatar os itens
    # Formatar os itens
    for item in items:
        # Dividir a string em pedaços de 10 caracteres
        # chunks = [item['content'][i:i + 10] for i in range(0, len(item['content']), 10)]
        chunks = item['content'].split(' ')
        pairs = []
        for i in range(0, len(chunks), 2):
            if i + 1 < len(chunks):
                pairs.append(chunks[i] + ' ' + chunks[i + 1])
            else:
                pairs.append(chunks[i])

        # Juntar os pedaços com a tag <br>
        content_with_breaks = '<br>'.join(pairs)

        # Contar a quantidade de quebras de linha
        line_count = len(pairs)  # +1 para a primeira linha

        # Definir a altura da div com base na quantidade de linhas
        height = line_count * 20  # Supondo que cada linha tenha 20px de altura

        item['content'] = f"<div style='width:150px; height:{height}px; word-wrap: break-word; font-size: 11px;'>{content_with_breaks}</div>"
    # Exibir a linha do tempo de atividades no Streamlit
    timeline = st_timeline(items, groups=[], options={}, height="700px")

    st.write("Item Selecionado:")
    st.write(timeline)