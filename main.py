
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import altair as alt
from datetime import datetime

import plotly.graph_objs as go
from datetime import datetime, timedelta



st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.title("Leonardo Carus de Oliveira")

st.write("Aqui você encontra informações sobre o Leonardo Carus de Oliveira. Tem o objetivo de monitorar as atividades do Leo e "
         "através de gráficos e relatórios, apresentar informações relevantes sobre a sua evolução no autismo.")
# Função para gerar dados de contribuição de exemplo
def generate_example_data(year=2024):
    # gerando uma data para cada dia do ano
    numdays = 365 + (1 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 0)  # account for leap year
    base = datetime(year, 1, 1)
    date_list = [base + timedelta(days=x) for x in range(numdays)]

    # gerando um número aleatório de contribuições para cada dia
    contributions = np.random.randint(0, 10, size=numdays)

    return date_list, contributions


# Gerando os dados de exemplo
dates, contribs = generate_example_data()

# Mapeamento de datas para eixos x (semana do ano) e y (dia da semana)
week_of_year = [date.isocalendar()[1] for date in dates]
day_of_week = [date.weekday() for date in dates]  # Monday is 0 and Sunday is 6

# Criar um calendário de contribuições usando Heatmap
heatmap = go.Heatmap(
    x=week_of_year,
    y=day_of_week,
    z=contribs,
    type='heatmap',
    colorscale='Greens'
)

# Criar a linha do tempo de atividades usando Bar
activity_data = {
    'MilanoJunior/leonardo': {'commits': 3, 'date_created': '2024-04-01'},
    'MilanoJunior/estudos_estatisticos': {'commits': 2, 'date_created': '2024-04-02'}
}

bar = go.Bar(
    x=[repo_data['commits'] for repo_data in activity_data.values()],
    y=list(activity_data.keys()),
    orientation='h'
)

# Exibir o gráfico de calor no Streamlit
st.plotly_chart(go.Figure(data=[heatmap]), use_container_width=True)

# Exibir a linha do tempo de atividades no Streamlit
st.plotly_chart(go.Figure(data=[bar]), use_container_width=True)

# # Simulando dados de exemplo para o calendário de contribuições
# contribs = np.random.randint(0, 5, (365,)) # 365 dias no ano, número de contribuições por dia
# dates = [np.datetime64(datetime(2024, 1, 1)) + np.timedelta64(i, 'D') for i in range(365)]
# # Adicionando zeros ao final do array para torná-lo divisível por 7
# contribs_padded = np.pad(contribs, (0, 7 - len(contribs) % 7), mode='constant')
#
# # Agora o reshape pode ser realizado sem erros
# contribs_calendar = np.reshape(contribs_padded, (-1, 7)) # 7 dias na semana
#
# # Criar o gráfico de calor para o calendário
# fig, ax = plt.subplots()
# ax.imshow(contribs_calendar, cmap='Greens')

# Ajustar os detalhes do gráfico como títulos, eixos, etc.
# ...

# # Exibir o calendário de contribuições no Streamlit
# st.pyplot(fig)
#
# # Simulando dados de exemplo para a linha do tempo de atividades
# activities = {
#     'MilanoJunior/leonardo': 3,
#     'MilanoJunior/estudos_estatisticos': 2,
# }
#
# # Criar a linha do tempo de atividades
# fig, ax = plt.subplots()
# for i, (repo, commits) in enumerate(activities.items()):
#     ax.broken_barh([(0, commits)], (i-0.4, 0.8), facecolors='tab:green')

# Ajustar os detalhes do gráfico como títulos, eixos, etc.
# ...

# Exibir a linha do tempo no Streamlit
# st.pyplot(fig)


prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")

# chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
#
# c = (
#    alt.Chart(chart_data)
#    .mark_circle()
#    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
# )
#
# st.altair_chart(c, use_container_width=True)




