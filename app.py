import streamlit as st
import pandas as pd

# Título da aplicação
st.title("Comparação de Arquivos Excel com Streamlit")

# Função para carregar arquivos
def carregar_arquivo(mensagem):
    st.write(mensagem)
    arquivo = st.file_uploader(mensagem, type=['xls', 'xlsx'])
    if arquivo:
        try:
            # Verifica a extensão do arquivo
            if arquivo.name.endswith('.xls'):
                df = pd.read_excel(arquivo, engine='xlrd')  # Para arquivos .xls
            else:
                df = pd.read_excel(arquivo)  # Para arquivos .xlsx
            st.success(f"Arquivo {arquivo.name} carregado com sucesso!")
            return df
        except Exception as e:
            st.error(f"Erro ao carregar o arquivo: {e}")
            return None
    else:
        st.warning("Nenhum arquivo foi carregado.")
        return None

# Carregar o primeiro arquivo
df1 = carregar_arquivo("Faça o upload do primeiro arquivo (Ex.: Base de Créditos):")

if df1 is not None:
    # Exibir o primeiro DataFrame
    st.subheader("Primeiro arquivo carregado:")
    st.write(df1)

    # Carregar o segundo arquivo
    df2 = carregar_arquivo("Faça o upload do segundo arquivo (Ex.: Base de Débitos):")

    if df2 is not None:
        # Exibir o segundo DataFrame
        st.subheader("Segundo arquivo carregado:")
        st.write(df2)

        # Verificar e processar as colunas
        if 'debito' in df2.columns and 'credito' in df1.columns:
            # Adicionar a coluna 'teste' com base na verificação
            df2['teste'] = df2['debito'].isin(df1['credito'])
            st.subheader("Resultado da Comparação:")
            st.write(df2)
        else:
            st.error("Os arquivos devem conter as colunas 'debito' e 'credito'. Verifique os arquivos carregados.")
    else:
        st.warning("Nenhum arquivo carregado como Base de Débitos.")
else:
    st.warning("Nenhum arquivo carregado como Base de Créditos.")

