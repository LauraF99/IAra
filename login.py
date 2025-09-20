import streamlit as st
from controllers.usuario_controller import validar_login, criar_usuario

def exibir_formulario_login():
    """
    Exibe o formulário de login e retorna o estado de autenticação
    """
    st.set_page_config(page_title="IAra - Login", page_icon="🔒")
    
    st.title("🧜‍♀️ IAra")
    
    with st.form("login_form"):
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")
        
        col1, col2 = st.columns(2)
        
        with col1:
            login_submit = st.form_submit_button("Entrar", use_container_width=True)
        
        with col2:
            criar_conta_submit = st.form_submit_button("Criar Conta", use_container_width=True)
        
        if login_submit:
            if email and senha:
                if validar_login(email, senha):
                    st.session_state["authenticated"] = True
                    st.session_state["email"] = email
                    st.success("Login realizado com sucesso!")
                    st.rerun()
                else:
                    st.error("E-mail ou senha incorretos.")
            else:
                st.warning("Preencha e-mail e senha para entrar.")
        
        if criar_conta_submit:
            if email and senha:
                sucesso = criar_usuario(email, senha)
                if sucesso:
                    st.success("Usuário criado com sucesso! Faça login.")
                else:
                    st.error("Erro ao criar usuário. Tente outro e-mail.")
            else:
                st.warning("Preencha e-mail e senha para criar conta.")
    
    return st.session_state.get("authenticated", False)

def verificar_autenticacao():
    """
    Verifica se o usuário está autenticado, se não, exibe o login
    """
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
    
    if not st.session_state["authenticated"]:
        return exibir_formulario_login()
    return True
