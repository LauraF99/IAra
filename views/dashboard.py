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


    st.subheader("Lista de Alunos")
    st.dataframe(df[["ID", "Nome", "Data de Nascimento", "Idade"]])


    df_filtrado = df.dropna(subset=["Idade"])

    if not df_filtrado.empty:
  
        st.subheader("Distribuição de Idades")
        fig = px.histogram(df_filtrado, x="Idade", nbins=10, title="Distribuição de Idades dos Alunos")
        st.plotly_chart(fig)

  
    st.subheader("Quantidade de Alunos")
    st.metric("Total de Alunos", len(df))
