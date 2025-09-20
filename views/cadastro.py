import streamlit as st
import datetime
from controllers.estudante_controller import adicionar_estudante, listar_estudantes

def show():
    st.title("📚 Cadastro de Estudantes")
    
    with st.form("cadastro_form"):
        nome = st.text_input("Nome")
        data_nascimento = st.date_input(
            "Data de Nascimento",
            min_value=datetime.date(1900, 1, 1),  
            max_value=datetime.date.today(),     
        )
        submitted = st.form_submit_button("Cadastrar")

        if submitted:
            adicionar_estudante(nome, data_nascimento)
            st.success("✅ Estudante cadastrado com sucesso!")
    
    st.subheader("Lista de Estudantes")
    estudantes = listar_estudantes()
    for e in estudantes:
        st.write(f"👤 {e.nome}")
