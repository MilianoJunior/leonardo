'''
Nome: Miliano Fernandes de Oliveira Junior
Data início: 06/05/2024
Data atualização: 06/05/2024
Descrição: Este é um aplicativo para monitorar e persisitir as atividades de crianças autistas.
O aplicativo tem o objetivo de gerar informações através de gráficos e relatórios que auxiliem os pais e profissionais a entenderem o comportamento e evolução da criança.
'''
import time
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import altair as alt
from libs.componentes import generate_example_data, heatmap, timeline
from libs.funcoes import get_idade, import_dados, salvar_dados, generate_data


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

col1, col2 = st.columns([.3, .7])

with col1:
    st.subheader("Leonardo Carus de Oliveira")

    st.divider()

    st.write("Aqui você encontra informações sobre o Leonardo Carus de Oliveira. Tem o objetivo de monitorar as atividades do Leo e "
         "através de gráficos e relatórios, apresentar informações relevantes sobre a sua evolução no autismo.")

    st.caption('Idade: ' + get_idade(ano_nascimento=2018, mes_nascimento=6, dia_nascimento=2))
    st.caption('Peso: 21 kg')
    st.caption('Altura: 1,10 m')

# Função para gerar dados de contribuição de exemplo
with col2:

    # Gerando os dados de exemplo
    dates, contribs = generate_example_data()
    df, datas, contribuicoes = generate_data()

    # Criar um gráfico de calor para visualizar as contribuições
    fig = heatmap(datas, contribuicoes)

    # Exibir o gráfico de calor no Streamlit
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Registro de atividades do Leonardo")
col11, col22, col33 = st.columns([.33, .33, .33])

with col11:
    # selecionar as atividades
    atividade = st.selectbox("Selecione as atividades", ["Alimentação","Atividade escola","Briga na escola","Medico","Reação","Interação","Brincar","Dentista","Estudar", "Comer", "Dormir", "Tomar banho"], default=["Brincar"])
with col22:
    # selecionar a data
    date = st.date_input("Data da atividade", value=pd.to_datetime('today'))

with col33:
    arquivo = uploaded_file = st.file_uploader("Anexar arquivo")


with st.container(height=250):
    # escrever uma observação
    texto = st.text_area("Observação", "Escreva aqui suas observações sobre a atividade")
    # with col32:
    btn_salvar = st.button("Salvar atividade")

    # styles
    styles = {
        "Alimentação": "background-color: #008000; color: black",  # Verde
        "Atividade escola": "background-color: #0000FF; color: white",  # Azul
        "Briga na escola": "background-color: #FF0000; color: white",  # Vermelho
        "Medico": "background-color: #800080; color: white",  # Roxo
        'Reação': "background-color: #FFFF00; color: black",  # Amarelo
        'Interação': "background-color: #FFA500; color: black",  # Laranja
        'Brincar': "background-color: #00FFFF; color: black",  # Ciano
        'Estudar': "background-color: #008080; color: white",  # Verde-azulado
        'Comer': "background-color: #FF00FF; color: black",  # Magenta
        'Dormir': "background-color: #000080; color: white",  # Azul marinho
        'Tomar banho': "background-color: #808000; color: white"  # Oliva
    }

    if btn_salvar:
        data = {
            'start':date.strftime('%Y-%m-%d %H:%M:%S'),
            'content':texto,
            'group':atividade[0],
            'style':styles.get(atividade[0], "color: red; background-color: pink;")

        }
        df = salvar_dados(data=data)
        df, datas, contribuicoes = generate_data()
        if df.empty:
            st.success("Atividade salva com sucesso!")
            time.sleep(2)
            st.rerun()
        else:
            st.error("Erro ao salvar a atividade!")
            time.sleep(2)
            st.rerun()
        for i in range(len(df)):
            st.write(str(df.iloc[i]))

# inserir timeline
with st.container():
    st.subheader("Timeline de atividades")
    timeline(df)






# # Mapeamento de datas para eixos x (semana do ano) e y (dia da semana)
# week_of_year = [date.isocalendar()[1] for date in dates]
# day_of_week = [date.weekday() for date in dates]  # Monday is 0 and Sunday is 6
#
# # Criar um calendário de contribuições usando Heatmap
# heatmap = go.Heatmap(
#     x=week_of_year,
#     y=day_of_week,
#     z=contribs,
#     type='heatmap',
#     colorscale='Greens'
# )

# # Criar a linha do tempo de atividades usando Bar
# activity_data = {
#     'MilanoJunior/leonardo': {'commits': 3, 'date_created': '2024-04-01'},
#     'MilanoJunior/estudos_estatisticos': {'commits': 2, 'date_created': '2024-04-02'}
# }
#
# bar = go.Bar(
#     x=[repo_data['commits'] for repo_data in activity_data.values()],
#     y=list(activity_data.keys()),
#     orientation='h'
# )
#
#
#
# # Exibir a linha do tempo de atividades no Streamlit
# st.plotly_chart(go.Figure(data=[bar]), use_container_width=True)
#
#
#
#
# prompt = st.chat_input("Say something")
# if prompt:
#     st.write(f"User has sent the following prompt: {prompt}")

# if '__name__' == '__main__':


# chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
#
# c = (
#    alt.Chart(chart_data)
#    .mark_circle()
#    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
# )
#
# st.altair_chart(c, use_container_width=True)






# import pyuac
#
# def main():
#     print("Executando como administrador.")
#     # Seu código aqui
#
# if __name__ == "__main__":
#     if not pyuac.isUserAdmin():
#         print("Reiniciando como administrador!")
#         pyuac.runAsAdmin()
#     else:
#         main()




#
# from pynput import mouse
# import pyautogui
#
# # Sua função para lidar com o clique do botão direito do mouse
# def on_click(x, y, button, pressed):
#     if button == mouse.Button.right and pressed:
#         # Digite suas credenciais quando o botão direito do mouse for clicado
#         pyautogui.write('seu_usuario')
#         pyautogui.press('tab')  # pressione a tecla Tab para ir para o campo da senha
#         pyautogui.write('sua_senha')
#         pyautogui.press('enter')  # pressione Enter para enviar o formulário
#
# # Inicie o ouvinte do mouse
# with mouse.Listener(on_click=on_click) as listener:
#     listener.join()
#
#
# Test-LocalConnection -UserName tecnico -WordList top.txt
#
# Start-Process -FilePath "C:\Program Files\Google\Chrome\Application\chrome.exe" -ArgumentList "https://www.google.com" -verb RunAs -PassThru
#
#


# import time
# import pygetwindow as gw

#
# tempo_espera = 2
# cont = 0
# janelas = []
#
# while True:
#     # Lista todas as janelas abertas
#     todas_janelas = gw.getAllTitles()
#
#     time.sleep(tempo_espera)
#     cont += 1
#     # Imprime o nome de todas as janelas
#     for i, janela in enumerate(todas_janelas):
#
#         if not janela in janelas:
#             print(i, janela)
#             janelas.append(janela)
#         # print(i, janela)
#
#     if  cont > 10:
#         break
#
# print(janelas)
# # Lista todas as janelas abertas
# todas_janelas = gw.getAllTitles()
# janelas = []
# # Imprime o nome de todas as janelas
# for i, janela in enumerate(todas_janelas):
#     janelas.append(janela)
#     if not janela in janelas:
#         print(i, janela)
#     # print(i, janela)
#
# # Tempo para o script esperar antes de começar (em segundos)
#
#
# # Nome da janela que você quer fechar
# nome_janela = 'Sistema e Segurança'



# # Encontra a janela
# janela = pyautogui.getWindowsWithTitle(nome_janela)[0]
#
# print(janela)
#
# # Fecha a janela
# janela.close()

# '''
# import os
#
# '''
# Pode implementar a estrutura de pastas e arquivos conforme abaixo:
#
# projeto/
#     libs/
#         elementos_graficos.py
#         funcoes_processamento.py
#     main.py
#
# '''
#
# # importar bibliotecas do python
# import os
#
# # importar as suas bibliotecas ou módulos
# from libs.elementos_graficos import *
# from libs.funcoes_processamento import calcular_media, calcular_soma
#
# # pasta absoluta do projeto
# path_absoluta = os.getcwd()
# print(path_absoluta)
# # pasta do projeto
#
# var1 = 10
# var2 = 20
#
# # calcular a média
# media = calcular_media(var1, var2)
# print(f'A média é: {media}')
#
# # calcular a soma
# soma = calcular_soma(var1, var2)
# print(f'A soma é: {soma}')
#
# # criar um gráfico de barras
# criar_grafico_barras([10, 20, 30], ['A', 'B', 'C'], 'Gráfico de Barras', 'Eixo X', 'Eixo Y')
# '''


