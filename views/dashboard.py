import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
from controllers.estudante_controller import listar_estudantes  


def calcular_idade(data_nascimento):
    if data_nascimento is None:
        return None  
    hoje = datetime.now()
    nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d")
    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
    return idade


def show():
    st.title("📊 Dashboard de Alunos")

   
    alunos = listar_estudantes()

    if not alunos:
        st.warning("Não há alunos cadastrados.")
        return

 
    df = pd.DataFrame([{
        "ID": aluno.id,
        "Nome": aluno.nome,
        "Data de Nascimento": aluno.data_nascimento
    } for aluno in alunos])

   
    df["Idade"] = df["Data de Nascimento"].apply(calcular_idade)
    
    # --- Filtros ---
    st.sidebar.header("Filtros")

    nome_filtro = st.sidebar.text_input("Filtrar por nome")
    idade_min = st.sidebar.number_input("Idade mínima", min_value=0, max_value=100, value=0)
    idade_max = st.sidebar.number_input("Idade máxima", min_value=0, max_value=100, value=100)
    data_inicio = st.sidebar.date_input("Data de nascimento inicial", value=datetime(1990, 1, 1))
    data_fim = st.sidebar.date_input("Data de nascimento final", value=datetime.now())

    if nome_filtro:
        df = df[df["Nome"].str.contains(nome_filtro, case=False)]

    if idade_min or idade_max:
        df = df[(df["Idade"] >= idade_min) & (df["Idade"] <= idade_max)]

    if data_inicio or data_fim:
        df = df[
            (pd.to_datetime(df["Data de Nascimento"], errors="coerce") >= pd.to_datetime(data_inicio)) &
            (pd.to_datetime(df["Data de Nascimento"], errors="coerce") <= pd.to_datetime(data_fim))
        ]


    st.subheader("Lista de Alunos")
    st.dataframe(df[["ID", "Nome", "Data de Nascimento", "Idade"]])


    df_filtrado = df.dropna(subset=["Idade"])

    if not df_filtrado.empty:
  
        st.subheader("Distribuição de Idades")
        fig = px.histogram(df_filtrado, x="Idade", nbins=10, title="Distribuição de Idades dos Alunos")
        st.plotly_chart(fig)

  
    st.subheader("Quantidade de Alunos")
    st.metric("Total de Alunos", len(df))
