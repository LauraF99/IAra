import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
from controllers.estudante_controller import listar_estudantes  # Importa a função do controller

# Função para calcular a idade com base na data de nascimento
def calcular_idade(data_nascimento):
    if data_nascimento is None:
        return None  # Retorna None se a data não estiver cadastrada
    hoje = datetime.now()
    nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d")
    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
    return idade

# Função para exibir o dashboard
def show():
    st.title("📊 Dashboard de Alunos")

    # Busca os dados dos alunos usando a função do controller
    alunos = listar_estudantes()

    if not alunos:
        st.warning("Não há alunos cadastrados.")
        return

    # Converte os dados para um DataFrame do Pandas
    df = pd.DataFrame([{
        "ID": aluno.id,
        "Nome": aluno.nome,
        "Data de Nascimento": aluno.data_nascimento
    } for aluno in alunos])

    # Adiciona uma coluna de idade (lidando com None)
    df["Idade"] = df["Data de Nascimento"].apply(calcular_idade)

    # Exibe a tabela de alunos
    st.subheader("Lista de Alunos")
    st.dataframe(df[["ID", "Nome", "Data de Nascimento", "Idade"]])

    # Filtra apenas alunos com idade calculada para o gráfico
    df_filtrado = df.dropna(subset=["Idade"])

    if not df_filtrado.empty:
        # Gráfico de distribuição de idades
        st.subheader("Distribuição de Idades")
        fig = px.histogram(df_filtrado, x="Idade", nbins=10, title="Distribuição de Idades dos Alunos")
        st.plotly_chart(fig)

    # Gráfico de quantidade de alunos
    st.subheader("Quantidade de Alunos")
    st.metric("Total de Alunos", len(df))
