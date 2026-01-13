import streamlit as st

# Configuração Específica desta Página
st.set_page_config(
    page_title="Dashboard Operacional",
    page_icon="📊",
    layout="wide" # Dashboards precisam de espaço, então usamos wide
)

st.title("Dashboard de Controle (H1)")
st.caption("Módulo de Análise Tática")

st.header("Indicadores de Desempenho (H2)")

# Simulando uma separação em colunas (layout básico)
col1, col2 = st.columns(2)

with col1:
    st.subheader("Métricas (H3)")
    st.write("Aqui entrarão os gráficos e KPIs futuramente.")
    st.text("Log: Dados carregados via CSV.")

with col2:
    st.subheader("Cálculos (H3)")
    # Exemplo de LaTeX movido para cá
    st.latex(r'''
    I_{criminalidade} = \frac{\sqrt{Ocorrências}}{Efetivo \times \text{Área}}
    ''')