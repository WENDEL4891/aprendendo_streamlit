import streamlit as st

# Configuração da Página Principal
st.set_page_config(
    page_title="Início - Sistema PM",
    page_icon="🏠",
    layout="centered", # Capas geralmente ficam melhores centralizadas
    initial_sidebar_state="expanded"
)

# Conteúdo da Home
st.title("Bem-vindo ao Sistema Integrado")
st.write("Esta é a página principal. Utilize o menu lateral para navegar entre os módulos.")

st.divider()

st.markdown("""
### 🗺️ Mapa do Sistema:
* **🏠 Início:** Esta página de apresentação.
* **📊 Análise:** Dashboards, indicadores e fórmulas (conteúdo técnico).
""")

# Dica na Sidebar (aparece em todas as páginas se colocado aqui, mas o menu nativo fica acima)
with st.sidebar:
    st.info("💡 O menu de navegação acima é gerado automaticamente pela pasta 'pages'.")