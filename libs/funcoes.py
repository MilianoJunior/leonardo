from datetime import date
import os
import pandas as pd
import streamlit as st
from datetime import datetime, timedelta
import numpy as np


def generate_data(year=2024):
    # gerando uma data para cada dia do ano
    numdays = 365 + (1 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 0)  # account for leap year
    base = datetime(year, 1, 1)
    date_list = [base + timedelta(days=x) for x in range(numdays)]

    # importando os dados
    df = import_dados()

    # Primeiro, certifique-se de que a coluna 'start' esteja no formato correto de data
    df['start'] = pd.to_datetime(df['start'])

    # Crie um novo dataframe que conta as ocorrências de cada data
    contribuicoes = df['start'].value_counts()
    contrib = np.zeros(numdays)
    for i in contribuicoes.index:
        for j in range(len(date_list)):
            if i == date_list[j]:
                contrib[j] = contribuicoes[i]

    return df, date_list, contrib

def get_idade(ano_nascimento, mes_nascimento, dia_nascimento):
    '''Retornar a idade no formato de anos completos, meses e dias, dado o ano, mês e dia de nascimento.'''
    hoje = date.today()
    nascimento = date(ano_nascimento, mes_nascimento, dia_nascimento)

    anos = hoje.year - nascimento.year
    meses = hoje.month - nascimento.month
    dias = hoje.day - nascimento.day

    if dias < 0:
        meses -= 1
        dias += 30  # Aproximação

    if meses < 0:
        anos -= 1
        meses += 12

    return f"{anos} anos {meses} meses e {dias} dias"

def import_dados(nome_arquivo='data.csv'):
    '''Importar dados de um arquivo CSV.'''
    path = os.path.join('data', nome_arquivo)

    if not os.path.exists(path):
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")

    return pd.read_csv(path)

def salvar_dados(data: dict, nome_arquivo='data.csv'):
    '''Salvar dados em um arquivo CSV.'''
    try:
        # criar o caminho do arquivo
        path = os.path.join('data', nome_arquivo)

        # importar os dados existentes
        df = import_dados(nome_arquivo)

        # adicionar os novos dados
        dts = [len(df)] + list(data.values())

        # adicionar os novos dados
        df.loc[len(df)] = dts

        # salvar os dados
        df.to_csv(path, index=False)

        return df
    except Exception as e:
        return False
