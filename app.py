import streamlit as st
from views import cadastro, conteudo, dashboard, documentos
from utils.db import init_db
from login import verificar_autenticacao
# Inicializa banco
init_db()

# Verifica autenticação - se não estiver autenticado, mostra login
if not verificar_autenticacao():
    st.stop()  # Para a execução aqui se não estiver autenticado

# SE CHEGOU ATÉ AQUI, O USUÁRIO ESTÁ AUTENTICADO


st.title("🧜‍♀️ IAra")
# Menu
st.sidebar.title("📌 Menu")
opcao = st.sidebar.radio("Navegação", ["Cadastro","Dashboard", "Conteúdo","Documentos"])

if opcao == "Cadastro":
    cadastro.show()
elif opcao == "Conteúdo":
    conteudo.show()
elif opcao == "Dashboard":
    dashboard.show()
elif opcao == "Documentos":
    documentos.show()

# Botão de logout
if st.button("Sair"):
    st.session_state["authenticated"] = False
    st.session_state["email"] = None
    st.rerun()